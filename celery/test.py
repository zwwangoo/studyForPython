from tasks import add

re = add.apply_async((2, 2), queue='lopri', countdown=10)

print re.status