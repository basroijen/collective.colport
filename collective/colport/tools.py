try:
    # Plone 4
    from App.class_init import InitializeClass
except ImportError:
    #BBB Plone < 4
    from Globals import InitializeClass
from OFS.SimpleItem import SimpleItem
from AccessControl import ClassSecurityInfo
from OFS.PropertyManager import PropertyManager
import csv
import time  # imports on seperate lines to keep pep8 happy
from cStringIO import StringIO
from Products.CMFCore.utils import UniqueObject

from collective.colport import config


class colportTool(UniqueObject, SimpleItem, PropertyManager):
    """
    This tool handles the exportation of collection fields
    """

    id = 'colport_tool'
    meta_type = 'ColportTool'
    title = 'Collection Exporter Tool'
    plone_tool = True

    ## Define properties
    _properties = ({'id': 'csv_delimiter', 'type': 'string', 'mode': 'rw'},
                   {'id': 'csv_quoting', 'type': 'string', 'mode': 'rw'},
                   {'id': 'csv_quotechar', 'type': 'string', 'mode': 'rw'},
                   {'id': 'csv_skipinitialspace', 'type': 'boolean', \
                    'mode': 'rw'},
                  )

    ## Set initial values
    csv_delimiter = ';'
    csv_quoting = 'QUOTE_ALL'
    csv_quotechar = '"'
    csv_skipinitialspace = False

    manage_options = (PropertyManager.manage_options
                      + SimpleItem.manage_options)

    ## Security shortcuts
    security = ClassSecurityInfo()

    security.declareProtected("View", "export_as_csv")

    def export_as_csv(self):
        """
        Modify keywords of object
        """
        parent = self.aq_parent
        fields = parent.getCustomViewFields()

        vocab = parent.listMetaDataFields(False)
        data = [[vocab.getValue(field, field) for field in fields]]

        items = parent.queryCatalog()
        for item in items:
            line = [getattr(item, field, "") for field in fields]
            # make entries exportable
            line = [self._processEntry(e) for e in line]
            data.append(line)

        return self.export_csv(parent.getId(), data)

    def _processEntry(self, entry):
        """
        some processing to clean up entries
        """
        # normalize to list
        result = []
        if not isinstance(entry, (list, tuple)):
            entry = [entry, ]
        for e in entry:
            if e is None:
                e = ''
            if isinstance(e, unicode):
                e = e.encode('utf-8')
            if not isinstance(e, str):
                e = str(e)
            result.append(e)
        return "\n".join(result)

    security.declarePrivate("export_csv")

    def export_csv(self, name, data):
        """
        Do a CSV export from a Python list
        """
        buffer = StringIO()
        # Set default values
        quoting=csv.QUOTE_ALL
#        csv_delimiter = ';'
#        if self.csv_delimiter != 1:
#            csv_delimiter = self.csv_delimiter
        if self.csv_quoting == 'QUOTE_MINIMAL':
            quoting = csv.QUOTE_MINIMAL
        if self.csv_quoting == 'QUOTE_NONNUMERIC':
            quoting = csv.QUOTE_NONNUMERIC
        if self.csv_quoting == 'QUOTE_NONE':
            quoting = csv.QUOTE_NONE
        try:
            writer = csv.writer(buffer, delimiter=self.csv_delimiter, \
                     quotechar=self.csv_quotechar, skipinitialspace=\
                     self.csv_skipinitialspace, quoting=quoting)
            for row in data:
                writer.writerow(row)
            value = buffer.getvalue()
            value = unicode(value, "utf-8").encode("iso-8859-1", "replace")
            self.REQUEST.RESPONSE.setHeader('Content-Type', 'text/csv')
            self.REQUEST.RESPONSE.setHeader('Content-Disposition', \
                                            'attachment;filename=%s-%s.csv' % \
                                       (name, time.strftime("%d-%m-%Y-%H:%M")))
        except Exception:
            # FIXME: We probably need to inform the user that an error
            #        occured instead of only logging it
            self.plone_log("%s: Error while creating CSV-file, probably an \
empty property in the colport_tool!" % (config.PROJECTNAME))
            return
        return value

InitializeClass(colportTool)
