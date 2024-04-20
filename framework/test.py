# import hmac
# import hashlib
#
# def generate_appsecret_proof(access_token, app_secret):
#     # Encode access_token and app_secret to bytes
#     access_token_bytes = access_token.encode('utf-8')
#     app_secret_bytes = app_secret.encode('utf-8')
#
#     # Generate HMAC hash using SHA256 algorithm
#     hmac_hash = hmac.new(app_secret_bytes, access_token_bytes, hashlib.sha256)
#
#     # Get the hexadecimal representation of the hash
#     appsecret_proof = hmac_hash.hexdigest()
#
#     return appsecret_proof
#
# app_secret = "2526507fe2d6a89c36044c1041c9f09e"
# # access_token = "EAAW41eVbZAMgBO7Wauyd7fZCInPGHwZCJJ6XDQEsZBfiAp2R7FnYZBf6PoswDu26pG7EekSBofSBe7SrDT9JQ1kplODZBf6u6Y4KwhImj6QhQlE1DhEgQOZBai08f9zcAaThDkle7QVlvnD9v0Y7j79exQjS1yNhmMpZA6adqlofVWYj1SMudH4ENN0ZD"
# access_token  = "EAARWyNawNqwBO9bon7d9Cph7JIGscmYhSuW3gQXQSYh9IIpr0x2jgZAIWjXg3L0i9eEOAucRdcoPO3bZB0xdMZCBDRKtNcafo8hRT59k62FQTo7qN1NjmsvnaZAwZCf60GbRlm7BZBp4Lso3IpOiU10ciHSynZAFUztOo2GH3VYfKQaMcKgpQrRL9nVepNXGAgX6eqCDR2wfGDBuVkZD"
# appsecret_proof = generate_appsecret_proof(access_token, app_secret)
# print(appsecret_proof)

from django.apps import apps
from user.models import User
from django.apps import apps
# from django.contrib.auth.models import User

def get_related_names_with_user_foreign_key():
    user_relations = []
    for model in apps.get_models():
        for field in model._meta.fields:
            if field.related_model == User:
                # Get the reverse relationship from the related model
                related_name = field.remote_field.related_name
                user_relations.append((model.__name__, related_name))
    return user_relations

user_related_names = get_related_names_with_user_foreign_key()
print("Models with User as a foreign key and their related names:")
for model_name, related_name in user_related_names:
    print(f"Model: {model_name}, Related Name: {related_name}")
# def get_tables_with_user_foreign_key():
#     user_tables = []
#     for model in apps.get_models():
#         for field in model._meta.fields:
#             if field.related_model == User:
#                 user_tables.append(model._meta.db_table)
#                 break
#     return user_tables
#
# user_tables = get_tables_with_user_foreign_key()
# print("Tables with User as a foreign key:")
# print(user_tables)