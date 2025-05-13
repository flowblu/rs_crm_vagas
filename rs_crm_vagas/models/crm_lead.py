from odoo import api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def action_create_applicant_from_vaga(self):
        self.ensure_one()

        applicant_vals = {
            'name': self.job_title or self.name,
            'department_id': self.department_id.id if self.department_id else False,
            'partner_name': self.partner_name,
            'email_from': self.email_from,
            'crm_lead_id': self.id,  # se for criar esse campo customizado
            'source_id': self.source_id.id if self.source_id else False,
            'description': self.required_skills,
        }

        applicant = self.env['hr.applicant'].create(applicant_vals)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'hr.applicant',
            'res_id': applicant.id,
            'view_mode': 'form',
            'target': 'current',
        }
