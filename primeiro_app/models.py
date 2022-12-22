from django.db import models


class Autor(models.Model):
    nome = models.CharField("Nome Completo", max_length=200)
    email = models.EmailField("Email", blank=True, null=True)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField("Categoria", max_length=200)
    descricao = models.TextField("descrição")

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField("Título", max_length=200)
    autor = models.ManyToManyField(Autor)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria", blank=True, null=True)
    data_publicacao = models.DateField(blank=True, null=True)
    edicao = models.CharField("Edição", max_length=200, blank=True, null=True)
    genero = models.CharField("Gênero textual", max_length=200, blank=True, null=True)
    editora = models.CharField("Editora", max_length=200, blank=True, null=True)
    valor = models.DecimalField("Valor", max_digits=7, decimal_places=2, default=99.99)
    descricao = models.TextField(blank=True, null=True)
    isbn = models.CharField("ISBN", max_length=13, unique=True, help_text="13 Caracteres <a "
                                                                          "href='https://www.isbn-international.org"
                                                                          "/content/what-isbn""'>ISBN number</a>")

    class Meta:
        verbose_name_plural = 'Livros'

    def _str_(self):
        return self.titulo


class Usuario(models.Model):
        SEXO_CHOICES = (
            ('M', u'Masculino'),
            ('F', u'Feminino'),
            ('N', u'Não Declarar'),
        )

        ESTADO_CIVIL_CHOICES = (
            ('S', u'Solteiro'),
            ('C', u'Casado'),
            ('D', u'Divorciado'),
            ('v', u'Viúv(o/a)'),
        )

        nome = models.CharField("Nome Completo", max_length=200)
        data_nasc = models.DateField()
        cpf = models.CharField("CPF", max_length=120)
        email = models.EmailField("Email")
        telefone = models.IntegerField("Telefone")
        sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
        estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES)

        def _str_(self):
            return self.cpf


class Endereco(models.Model):
    cep = models.IntegerField("CEP")
    rua = models.CharField("Rua", max_length=120)
    numero = models.IntegerField("Numero")
    complemento = models.TextField(blank=True, null=True)
