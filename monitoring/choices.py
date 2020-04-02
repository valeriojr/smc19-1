symptoms = [
    ('CA', 'Cansaço'),
    ('CN', 'Congestão nasal'),
    ('DI', 'Diarreia'),
    ('SB', 'Dificuldade respiratória'),
    ('ST', 'Dor de garganta'),
    ('DC', 'Dor de cabeça'),
    ('AP', 'Dores no corpo'),
    ('FA', 'Falta de apetite'), # famoso fastio
    ('FV', 'Febre'),
    ('RN', 'Nariz escorrendo'),
    ('NA', 'Náusea'),
    ('TP', 'Tosse produtiva'),
    ('TS', 'Tosse seca'),
    ('VO', 'Vômitos'),
]

intensities = [
    ('', 'Não apresenta'),
    ('L', 'Leve'),
    ('M', 'Moderada'),
    ('H', 'Grave'),
]

genders = [
    ('F', 'Feminino'),
    ('M', 'Masculino'),
    ('N', 'Não quer declarar')
]

address_types = [
    ('HM', 'Residencial'),
    ('WK', 'Trabalho'),
    ('OT', 'Outro'),
]

# drugs = [
#     ('', 'Anti hipertensivo'),
#     ('', 'Imunossupressores'),
#     ('', 'Anti diabéticos'),
#     ('', 'Antibióticos'),
#     ('', 'Corticoide'),
#     ('', 'Anti inflamatório')
# ]

comorbidities = [
    ('Y', 'Artrite reumatóide'),
    ('A', 'Asma'),
    ('C', 'Bronquite crônica'),
    ('N', 'Câncer'),
    ('E', 'Demência'),
    ('D', 'Diabetes'),
    ('H', 'Doença cardíacas'),
    ('L', 'Doença crônica no fígado'),
    ('R', 'Doença renal crônica'),
    ('W', 'Doenças reumáticas'),
    ('P', 'Doença pulmonar crônica'),
    ('I', 'Imunosuprimido'),
    ('T', 'Hipertensão'),
    ('V', 'HIV+'),
    ('B', 'Obesidade'),
    ('U', 'Portador de Lúpus'),
]

countries = [
    ('CHN', 'China'),
    ('BRA', 'Brasil'),
    ('ESP', 'Espanha'),
    ('USA', 'Estados Unidos'),
    ('ITA', 'Itália'),
]

exposure = [
    ('confirmed_cases', 'Contato com casos confirmados'),
    ('suspect_cases', 'Contato com casos suspeitos'),
    ('foreign', 'Contato com pessoas que estiveram em locais com casos confirmados'),
]

results = [
    ('SR', 'Sem resposta'),
    ('PO', 'Positivo'),
    ('NE', 'Negativo'),
]

status = (
    ('N', 'Normal'),
    ('T', 'Testado'),
    ('S', 'Suspeito'),
    ('C', 'Confirmado'),
    ('M', 'Morto'),
    ('I', 'Imune'),
    ('H', 'Hospitalizado'),
    ('U', 'UTI')
)

action_choices = (
    ('C','CREATE'),
    ('D','DELETE'),
    ('U','UPDATE'),
)

model_choices = (
    ('PR','PROFILE'),
    ('AD','ADDRESS'),
    ('MO','MONITORING'),
    ('SY','SYMPTOM'),
    ('TR','TRIP'),
    ('RE','REQUEST'),
    ('HC', 'HEALTH CARE STATUS')
)

cities = (
    'Água Branca',
    'Anadia',
    'Arapiraca',
    'Atalaia',
    'Barra de Santo Antônio',
    'Barra de São Miguel',
    'Batalha',
    'Belém',
    'Belo Monte',
    'Boca da Mata',
    'Branquinha',
    'Cacimbinhas',
    'Cajueiro',
    'Campestre',
    'Campo Alegre',
    'Campo Grande',
    'Canapí',
    'Capela',
    'Carneiros',
    'Chã Preta',
    'Coité do Nóia',
    'Colônia Leopoldina',
    'Coqueiro Seco',
    'Coruripe',
    'Craíbas',
    'Delmiro Gouveia',
    'Dois Riachos',
    'Estrela de Alagoas',
    'Feira Grande',
    'Feliz Deserto',
    'Flexeiras',
    'Girau do Ponciano',
    'Ibateguara',
    'Igací',
    'Igreja Nova',
    'Inhapí',
    'Jacaré dos Homens',
    'Jacuípe',
    'Japaratinga',
    'Jaramataia',
    'Jequiá da Praia',
    'Joaquim Gomes',
    'Jundiá',
    'Junqueiro',
    'Lagoa da Canoa',
    'Limoeiro de Anadia',
    'Maceió',
    'Major Isidoro',
    'Mar Vermelho',
    'Maragogi',
    'Maravilha',
    'Marechal Deodoro',
    'Maribondo',
    'Mata Grande',
    'Matriz de Camaragibe',
    'Messias',
    'Minador do Negrão',
    'Monteirópolis',
    'Murici',
    'Novo Lino',
    'Olho D’Água das Flôres',
    'Olho D’Água do Casado',
    'Olho D’Água Grande',
    'Olivença',
    'Ouro Branco',
    'Palestina',
    'Palmeira dos Índios',
    'Pão de Açucar',
    'Pariconha',
    'Paripueira',
    'Passo de Camaragibe',
    'Paulo Jacinto',
    'Penedo',
    'Piaçabuçu',
    'Pilar',
    'Pindoba',
    'Piranhas',
    'Poço das Trincheiras',
    'Porto Calvo',
    'Porto de Pedras',
    'Porto Real do Colégio',
    'Quebrangulo',
    'Rio Largo',
    'Roteiro',
    'Santa Luzia do Norte',
    'Santana do Ipanema',
    'Santana do Mundaú',
    'São Brás',
    'São José da Laje',
    'São José da Tapera',
    'São Luiz do Quitunde',
    'São Miguel dos Campos',
    'São Miguel dos Milagres',
    'São Sebastião',
    'Satuba',
    'Senador Rui Palmeira',
    'Tanque D’Arca',
    'Taquarana',
    'Teotônio Vilela',
    'Traipu'
)
