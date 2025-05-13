from odoo import models, fields

class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    crm_lead_id = fields.Many2one('crm.lead', string="Origem Vaga CRM")
