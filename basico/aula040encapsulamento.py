# Encapsulamento (modificadores de acesso: public, protected, private)
# Python não tem modificadores de acesso
# Mas podemos seguir as seguintes convenções:
# (sem underline) = public
#   - Pode ser acessado de qualquer lugar

# (um underline) = protected
#   - não deve ser usado fora da classe ou subclasse

# (sem underline) = private
#   - 'Name mangling'(desfiguração de nomes)
#   - _NomeClasse__nome_attr_ou_method
#   - só deve ser usado na classe que foi criada
#   - Não deve ser usado em nenhum lugar

class Foo:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso é protegido'
        self.__provate = 'Isso é private'

    def metodo_publico(self):
        return 'metodo publico'

    def _metodo_protected(self):
        return '_metodo_protected'


f = Foo()
print(f.public)
