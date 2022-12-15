from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    database_backup_config = fields.Boolean("Database Auto Backup", config_parameter='db_backup.database_backup_config')
    delete_after = fields.Integer("Delete after", config_parameter='db_backup.delete_days')
