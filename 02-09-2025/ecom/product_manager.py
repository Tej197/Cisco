products = []


def create_product(product_id, name, description, category, tags, stock, price):
    global products
    products.append({
        'id': product_id,
        'name': name,
        'description': description,
        'category': category,
        'tags': tags,
        'stock': stock,
        'price': price
    })

def read_all_products():
    return products

def read_by_product_name(name):
    for i in range(len(products)):
        if products[i]['name'].lower() == name.lower():
            return i
    return -1

def update_product(product_id, name, description, category, tags, stock, price):
    global products
    index = read_by_id(product_id)
    if index != -1:
        products[index] = {
            'id': product_id,
            'name': name,
            'description': description,
            'category': category,
            'tags': tags,
            'stock': stock,
            'price': price
        }

def delete_product(name):
    global products
    index = read_by_product_name(name)
    if index != -1:
        products.pop(index)

def read_by_id(id):
    for i, prod in enumerate(products):
        if prod.get('id') == id:
            return i
    return -1

def read_by_product_tags(tag):
    results = []
    for i, prod in enumerate(products):
        if 'tags' in prod and tag.lower() in [t.lower() for t in prod['tags']]:
            results.append((i, prod))
    return results

def read_by_product_description(keyword):
    results = []
    for i, prod in enumerate(products):
        if 'description' in prod and keyword.lower() in prod['description'].lower():
            results.append((i, prod))
    return results