from django.shortcuts import render, redirect, get_object_or_404
from .models import Inventory, Clothing, Rack, Warehouse, Supplier, Supplies
from django.db.models import Max

def add_item(request):
    if request.method == "POST":
        supplier_name = request.POST.get('supplier')
        size = request.POST.get('size')
        color = request.POST.get('color')
        material = request.POST.get('material')
        type = request.POST.get('type')
        quantity = int(request.POST.get('quantity'))
        warehouse_id = int(request.POST.get('warehouse_id'))

        supplier, _ = Supplier.objects.get_or_create(
            supplier_name = supplier_name,
            defaults={
                'supplier_id': (Supplier.objects.aggregate(Max('supplier_id'))['supplier_id__max'] or 0) + 1
            }
        )
        
        new_clothing_id = (Clothing.objects.aggregate(Max('clothing_id'))['clothing_id__max'] or 0) + 1
        
        clothing = Clothing.objects.create(
            clothing_id=new_clothing_id,
            clothing_type=type,
            material=material,
            color=color,
            size=size
        )
        
        Supplies.objects.create(
            supplier_id=supplier.supplier_id,
            clothing_id=clothing.clothing_id
        )

        rack = Rack.objects.filter(warehouse_id=warehouse_id).first()

        if not rack:
            return redirect('inventory_view')
        
        new_inventory_id = (Inventory.objects.aggregate(Max('inventory_id'))['inventory_id__max'] or 0) + 1

        Inventory.objects.create(
            inventory_id=new_inventory_id,
            clothing=clothing,
            rack=rack,
            quantity=quantity
        )

    return redirect('inventory_view')

def sell_item(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(Inventory, inventory_id=item_id)
        item.delete()
        print("Deleting item id", item_id)
    return redirect('inventory_view')

def inventory_view(request):
    sort_by = request.GET.get('sort_by', 'clothing__size')  
    order = request.GET.get('order', 'asc')

    items = Inventory.objects.select_related('clothing', 'rack', 'rack__warehouse').all()

    if sort_by and order:
        if order == 'desc':
            sort_by = '-' + sort_by
        items = items.order_by(sort_by)

    search = request.GET.get('search', '')
    if search:
        items = items.filter(
            clothing__material__icontains=search
        )

    return render(request, 'index.html', {'items': items})