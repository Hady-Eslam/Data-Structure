from AssiociationList import AssiociationList

List = AssiociationList()

List.Insert('First', 'Hello')
List.Insert('Second', 'World')
List.Insert('Third', 'Hady')

print(List.Get('First'))
print(List.Get('Second'))
print(List.Get('Third'))

List.Delete('Second')

print(List.Get('Second'))
