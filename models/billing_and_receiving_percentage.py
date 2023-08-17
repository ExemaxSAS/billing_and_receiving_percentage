
from odoo import models, api, fields


class BillingAndReceivingPercentage(models.Model):
   
    _inherit = 'purchase.order'
         
    #campo porcentaje compras
    campo_porcentaje = fields.Float(string="Porcentaje Compras")   
    #campo porcentaje ventas
    campo_porcentaje_recep = fields.Float(string="Porcentaje Recepción")  
    


    #calculando el porcentaje de compras
    def calculo_porcentaje(self):
        var = 0
        fac = 0
        x = 0
        self.campo_porcentaje=0
        
        for ta in self.order_line: 
            var = var + ta.product_qty 
            fac = fac + ta.qty_invoiced
        if var > 0:
            self.campo_porcentaje = (fac / var)*100
        return self.campo_porcentaje
    #calculando porcentaje de recepcion
    #@api.depends('order_line.qty_received')    
    def calculo_porcentaje_re(self):
        var = 0
        rec = 0
        x=0
        self.campo_porcentaje_recep=0
        for ta in self.order_line: 
            var = var + ta.product_qty 
            rec = rec + ta.qty_received
        if var > 0:    
            self.campo_porcentaje_recep =(rec / var)*100    
        return self.campo_porcentaje_recep