import ldap, sys
from django_auth_ldap.config import ActiveDirectoryGroupType
#ldap.OPT_X_TLS_ALLOW

l = ldap.initialize('ldap://www.zflexldap.com') # or ldaps://
#l.start_tls_s()

#l.protocol_version=ldap.VERSION3
print('connected')
try:
    #l.start_tls_s()
    l.simple_bind_s("cn=ro_admin,ou=sysadmins,dc=zflexsoftware,dc=com", "zflexpass")
except ldap.LDAPError as e:
    #print(e.message['info'])
    print(e)
    """ if type(e.message) == dict and e.message.has_key('desc'):
        print(e.message['desc'])    
    else:
        print(e) """
    sys.exit()

l.simple_bind_s("cn=ro_admin,ou=sysadmins,dc=zflexsoftware,dc=com", "zflexpass")
print('connected')


users = l.search_s("ou=usa,o=company1,dc=zflexsoftware,dc=com",ldap.SCOPE_SUBTREE,'(objectclass=person)',attrlist=['uid','mail','sn','ou'])

uids=[]
emails=[]
sn=[]
ou=[]

for i in users:
    uids.append(i[-1].get('uid'))
    emails.append(i[-1].get('mail'))
    sn.append(i[-1].get('sn'))
    ou.append(i[0])
print(uids)
print(emails)
print(sn)
print(ou)
    



    
#attrlist=["uid", "sn","mail"]
