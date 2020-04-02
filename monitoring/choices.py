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
    ('AGUA', 'Água Branca'),
    ('ANADIA', 'Anadia'),
    ('ARAPIRACA', 'Arapiraca'),
    ('ATALAIA', 'Atalaia'),
    ('BSANTONIO', 'Barra de Santo Antônio'),
    ('BSMIGUEL', 'Barra de São Miguel'),
    ('BATALHA', 'Batalha'),
    ('BELEM', 'Belém'),
    ('BELO', 'Belo Monte'),
    ('BOCA', 'Boca da Mata'),
    ('BRANQUINHA', 'Branquinha'),
    ('CACIMBINHAS', 'Cacimbinhas'),
    ('CAJUEIRO', 'Cajueiro'),
    ('CAMPESTRE', 'Campestre'),
    ('CALEGRE', 'Campo Alegre'),
    ('CGRANDE', 'Campo Grande'),
    ('CANAPI', 'Canapí'),
    ('CAPELA', 'Capela'),
    ('CARNEIROS', 'Carneiros'),
    ('CHA', 'Chã Preta'),
    ('COITE', 'Coité do Nóia'),
    ('COLONIA', 'Colônia Leopoldina'),
    ('COQUEIRO', 'Coqueiro Seco'),
    ('CORURIPE', 'Coruripe'),
    ('CRAIBAS', 'Craíbas'),
    ('DELMIRO', 'Delmiro Gouveia'),
    ('DOIS', 'Dois Riachos'),
    ('ESTRELA', 'Estrela de Alagoas'),
    ('FEIRA', 'Feira Grande'),
    ('FELIZ', 'Feliz Deserto'),
    ('FLEXEIRAS', 'Flexeiras'),
    ('GIRAU', 'Girau do Ponciano'),
    ('IBATEGUARA', 'Ibateguara'),
    ('IGACI', 'Igací'),
    ('IGREJA', 'Igreja Nova'),
    ('INHAPI', 'Inhapí'),
    ('JACARE', 'Jacaré dos Homens'),
    ('JACUIPE', 'Jacuípe'),
    ('JAPARATINGA', 'Japaratinga'),
    ('JARAMATAIA', 'Jaramataia'),
    ('JEQUIA', 'Jequiá da Praia'),
    ('JOAQUIM', 'Joaquim Gomes'),
    ('JUNDIA', 'Jundiá'),
    ('JUNQUEIRO', 'Junqueiro'),
    ('LAGOA', 'Lagoa da Canoa'),
    ('LIMOEIRO', 'Limoeiro de Anadia'),
    ('MACEIO', 'Maceió'),
    ('MAJOR', 'Major Isidoro'),
    ('MAR', 'Mar Vermelho'),
    ('MARAGOGI', 'Maragogi'),
    ('MARAVILHA', 'Maravilha'),
    ('MARECHAL', 'Marechal Deodoro'),
    ('MARIBONDO', 'Maribondo'),
    ('MATA', 'Mata Grande'),
    ('MATRIZ', 'Matriz de Camaragibe'),
    ('MESSIAS', 'Messias'),
    ('MINADOR', 'Minador do Negrão'),
    ('MONTEIROPOLIS', 'Monteirópolis'),
    ('MURICI', 'Murici'),
    ('NOVO', 'Novo Lino'),
    ('ODAFLORES', 'Olho D’Água das Flôres'),
    ('ODACASADO', 'Olho D’Água do Casado'),
    ('ODAGRANDE', 'Olho D’Água Grande'),
    ('OLIVENCA', 'Olivença'),
    ('OURO', 'Ouro Branco'),
    ('PALESTINA', 'Palestina'),
    ('PALMEIRA', 'Palmeira dos Índios'),
    ('PAO', 'Pão de Açucar'),
    ('PARICONHA', 'Pariconha'),
    ('PARIPUEIRA', 'Paripueira'),
    ('PASSO', 'Passo de Camaragibe'),
    ('PAULO', 'Paulo Jacinto'),
    ('PENEDO', 'Penedo'),
    ('PIACABUCU', 'Piaçabuçu'),
    ('PILAR', 'Pilar'),
    ('PINDOBA', 'Pindoba'),
    ('PIRANHAS', 'Piranhas'),
    ('POCO', 'Poço das Trincheiras'),
    ('PCALVO', 'Porto Calvo'),
    ('PPEDRAS', 'Porto de Pedras'),
    ('PRCOLEGIO', 'Porto Real do Colégio'),
    ('QUEBRANGULO', 'Quebrangulo'),
    ('RIO', 'Rio Largo'),
    ('ROTEIRO', 'Roteiro'),
    ('SANTA', 'Santa Luzia do Norte'),
    ('SANTANAIP', 'Santana do Ipanema'),
    ('SANTANAMUN', 'Santana do Mundaú'),
    ('SBRAS', 'São Brás'),
    ('SJLAJE', 'São José da Laje'),
    ('SJTAPERA', 'São José da Tapera'),
    ('SLQUITUNDE', 'São Luiz do Quitunde'),
    ('SMCAMPOS', 'São Miguel dos Campos'),
    ('SMMILAGRES', 'São Miguel dos Milagres'),
    ('SSEBASTIAO', 'São Sebastião'),
    ('SATUBA', 'Satuba'),
    ('SENADOR', 'Senador Rui Palmeira'),
    ('TANQUE', 'Tanque D’Arca'),
    ('TAQUARANA', 'Taquarana'),
    ('TEOTONIO', 'Teotônio Vilela'),
    ('TRAIPU', 'Traipu')
)
