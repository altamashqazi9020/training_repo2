# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class BistaTraining(models.Model):
     _name = 'bista_training.bista_training'
     _description = 'bista_training.bista_training'

     name = fields.Char('Name', required=1 )
     value = fields.Integer('Score')
     date = fields.Date('Date of Exam',required=1)
     trainee_ids = fields.One2many('bista.trainee','training_batch_id',strings="Trainee" )

class Trainee(models.Model):
     _name = 'bista.trainee'
     _description = 'Training Master'

      #def create(self,vals):
     # def write(self,vals):
     # def unlike(self):

     @api.model
     def create(self,vals):
          print('@@@@',vals)
          return super(Trainee,self).create(vals)


     def write(self, vals):
          print('This is write Method', vals)
          return super(Trainee, self).write(vals)


     @api.constrains('email_2')
     def _check_email_2_values(self):
          if self.email_2 == 'altamashmmj@gmail.com':
               raise ValidationError(_('you are not allowded to enter this value'))

     def action_employed(self):
     #action function
        for rec in self:
             rec.state='employed'
        return True
     def action_reject(self):
          for rec in self:
               rec.state='rejected'

          return True

     name = fields.Char( 'Name' , required=1)
     email = fields.Char('Email')
     email_2 = fields.Char('Email2')
     trainee_id = fields.Char(string='Trainee ID',
                              default=lambda self: self.env['ir.sequence'].next_by_code('trainee.id'))
     training_batch_id = fields.Many2one('bista_training.bista_training' , string="Batch",help='this field is to full up batch details')

     image_1920 = fields.Image(string='image')
     state = fields.Selection([('new','New'),('employed','Employed'),('rejected','Rejected')],string="State",default='new')

     _sql_constraints = [
          ('email_unique','unique(email)', 'Email ID should be unique')
     ]
