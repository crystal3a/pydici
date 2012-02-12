# coding:utf-8
"""
Django administration setup
@author: Sébastien Renard <Sebastien.Renard@digitalfox.org>
@license: AGPL v3 or newer (http://www.gnu.org/licenses/agpl-3.0.html)
"""

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from ajax_select.admin import AjaxSelectAdmin

from pydici.billing.models import ClientBill, SupplierBill
from pydici.billing.forms import ClientBillForm, SupplierBillForm


#class BillAdmin(AjaxSelectAdmin):
class BillAdmin(AjaxSelectAdmin):
    list_display = ("id", "bill_id", "lead", "state", "amount", "creation_date", "due_date", "payment_date", "comment")
    ordering = ("-creation_date",)
    actions = None
    list_filter = ["state", "creation_date", "due_date", "payment_date", "previous_year_bill"]
    search_fields = ["lead__name", "lead__client__organisation__name", "comment",
                     "lead__paying_authority__contact__name", "lead__paying_authority__company__name",
                     "lead__client__contact__name", "lead__client__organisation__company__name"]


class ClientBillAdmin(BillAdmin):
    form = ClientBillForm
    fieldsets = [
                 (_("Description"), {"fields": ["lead", "bill_id", "bill_file"]}),
                 (_("Amounts"), {"fields": ["amount", "vat", "amount_with_vat", ]}),
                 (_("Dates"), {"fields": ["creation_date", "due_date", "payment_date", ]}),
                 (_("State"), {"fields": ["state", "previous_year_bill", "comment", ]}),
                 (_("Link with expenses"), {"fields": ["expenses", "expenses_with_vat", ]}),
                 ]


class SupplierBillAdmin(BillAdmin):
    form = SupplierBillForm
    search_fields = BillAdmin.search_fields + ["supplier_contact__name", "supplier__company__name"]
    fieldsets = [
                 (_("Description"), {"fields": ["supplier", "lead", "bill_id", "supplier_bill_id", "bill_file"]}),
                 (_("Amounts"), {"fields": ["amount", "vat", "amount_with_vat", ]}),
                 (_("Dates"), {"fields": ["creation_date", "due_date", "payment_date", ]}),
                 (_("State"), {"fields": ["state", "previous_year_bill", "comment", ]}),
                 (_("Link with expenses"), {"fields": ["expenses", "expenses_with_vat", ]}),
                 ]


admin.site.register(ClientBill, ClientBillAdmin)
admin.site.register(SupplierBill, SupplierBillAdmin)
