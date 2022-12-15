import os, time
import odoo
from odoo import models, fields, api
from datetime import datetime, date


class DbBackup(models.Model):
    _name = 'db.backup'
    _rec_name = 'database'
    database = fields.Char(string="Database", help="Database Name")
    directory = fields.Char(string="Directory", help="Directory to store backup.")

    def backup(self):
        res = self.env['db.backup'].search([])
        for rec in res:
            try:
                bkp_file = '%s_%s.dump' % (datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S"), rec.database)
                backup_file = os.path.join(rec.directory, bkp_file)
                f = open(backup_file, "wb")
                odoo.service.db.dump_db(rec.database, f, 'dump')
                f.close()
            except Exception as e:
                print("Exception", e)

    def remove_backup_database(self):
        res = self.env['db.backup'].search([])
        for rec in res:
            try:
                dir = rec.directory
                for f in os.listdir(dir):
                    fullpath = os.path.join(dir, f)
                    timestamp = os.stat(fullpath).st_ctime
                    create_time = datetime.fromtimestamp(timestamp)

                    if (datetime.now() - create_time).days >= int(
                            self.env['ir.config_parameter'].get_param('db_backup.delete_days')):
                        if os.path.isfile(fullpath) and ".dump" in f:
                            print("Delete: " + fullpath)
                            os.remove(fullpath)
            except Exception as e:
                print("Exception", e)
