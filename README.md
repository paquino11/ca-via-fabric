# Run?
```
python3 genCAs.py
```

# What it does?

(keep in mind that this is used for a Fabric Network deployment use case)

1. Create Org1 Identities
2. Enroll the CA admin
3. Register peer0
4. Register user
5. Register org admin
6. Registering the org admin
7. Generate the peer0 msp
8. Generate the peer0-tls certificates, use --csr.hosts to specify Subject Alternative Names
9. Generate the user msp
10. Generate the org admin msp
11. Generate CCP files for Org1

!!!! Its deployed to containers, one as a CA and other as a Organization
!!!! CA provides certification to Organization

# Where you can find it (ca, msp, tls, .cert, .pem)?

```
cd fabric-samples/test-network/organizations/
```

# How it is generated? (dont run, only run with python script)
```
bash fabric-samples/test-network/organizations/fabric-ca/registerEnroll.sh
```