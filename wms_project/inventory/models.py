from django.db import models

class Employee(models.Model):
    ssn = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    salary = models.IntegerField()
    emp_role = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Employee'


class Warehouse(models.Model):
    warehouse_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=100)
    regional_manager = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='regional_manager_ssn'
    )

    class Meta:
        managed = False
        db_table = 'Warehouse'


class Rack(models.Model):
    rack_id = models.IntegerField(primary_key=True)
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        db_column='warehouse_id'
    )
    aisle_section = models.CharField(max_length=50, blank=True, null=True)
    aisle_header = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Rack'


class Clothing(models.Model):
    clothing_id = models.IntegerField(primary_key=True)
    clothing_type = models.CharField(max_length=100)
    material = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Clothing'


class Supplier(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    supplier_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Supplier'


class Distributor(models.Model):
    distributor_id = models.IntegerField(primary_key=True)
    distributor_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Distributor'


class Inventory(models.Model):
    inventory_id = models.IntegerField(primary_key=True)
    clothing = models.ForeignKey(
        Clothing,
        on_delete=models.CASCADE,
        db_column='clothing_id'
    )
    rack = models.ForeignKey(
        Rack,
        on_delete=models.CASCADE,
        db_column='rack_id'
    )
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Inventory'


class Supplies(models.Model):
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        db_column='supplier_id'
    )
    clothing = models.ForeignKey(
        Clothing,
        on_delete=models.CASCADE,
        db_column='clothing_id'
    )

    class Meta:
        managed = False
        db_table = 'Supplies'
        unique_together = (('supplier', 'clothing'),)


class Distributes(models.Model):
    distributor = models.ForeignKey(
        Distributor,
        on_delete=models.CASCADE,
        db_column='distributor_id'
    )
    clothing = models.ForeignKey(
        Clothing,
        on_delete=models.CASCADE,
        db_column='clothing_id'
    )

    class Meta:
        managed = False
        db_table = 'Distributes'
        unique_together = (('distributor', 'clothing'),)