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
    ('AGUA', 'ÁGUA BRANCA'),
    ('ANADIA', 'ANADIA'),
    ('ARAPIRACA', 'ARAPIRACA'),
    ('ATALAIA', 'ATALAIA'),
    ('BSANTONIO', 'BARRA DE SANTO ANTÔNIO'),
    ('BSMIGUEL', 'BARRA DE SÃO MIGUEL'),
    ('BATALHA', 'BATALHA'),
    ('BELEM', 'BELÉM'),
    ('BELO', 'BELO MONTE'),
    ('BOCA', 'BOCA DA MATA'),
    ('BRANQUINHA', 'BRANQUINHA'),
    ('CACIMBINHAS', 'CACIMBINHAS'),
    ('CAJUEIRO', 'CAJUEIRO'),
    ('CAMPESTRE', 'CAMPESTRE'),
    ('CALEGRE', 'CAMPO ALEGRE'),
    ('CGRANDE', 'CAMPO GRANDE'),
    ('CANAPI', 'CANAPÍ'),
    ('CAPELA', 'CAPELA'),
    ('CARNEIROS', 'CARNEIROS'),
    ('CHA', 'CHÃ PRETA'),
    ('COITE', 'COITÉ DO NÓIA'),
    ('COLONIA', 'COLÔNIA LEOPOLDINA'),
    ('COQUEIRO', 'COQUEIRO SECO'),
    ('CORURIPE', 'CORURIPE'),
    ('CRAIBAS', 'CRAÍBAS'),
    ('DELMIRO', 'DELMIRO GOUVEIA'),
    ('DOIS', 'DOIS RIACHOS'),
    ('ESTRELA', 'ESTRELA DE ALAGOAS'),
    ('FEIRA', 'FEIRA GRANDE'),
    ('FELIZ', 'FELIZ DESERTO'),
    ('FLEXEIRAS', 'FLEXEIRAS'),
    ('GIRAU', 'GIRAU DO PONCIANO'),
    ('IBATEGUARA', 'IBATEGUARA'),
    ('IGACI', 'IGACÍ'),
    ('IGREJA', 'IGREJA NOVA'),
    ('INHAPI', 'INHAPÍ'),
    ('JACARE', 'JACARÉ DOS HOMENS'),
    ('JACUIPE', 'JACUÍPE'),
    ('JAPARATINGA', 'JAPARATINGA'),
    ('JARAMATAIA', 'JARAMATAIA'),
    ('JEQUIA', 'JEQUIÁ DA PRAIA'),
    ('JOAQUIM', 'JOAQUIM GOMES'),
    ('JUNDIA', 'JUNDIÁ'),
    ('JUNQUEIRO', 'JUNQUEIRO'),
    ('LAGOA', 'LAGOA DA CANOA'),
    ('LIMOEIRO', 'LIMOEIRO DE ANADIA'),
    ('MACEIO', 'MACEIÓ'),
    ('MAJOR', 'MAJOR ISIDORO'),
    ('MAR', 'MAR VERMELHO'),
    ('MARAGOGI', 'MARAGOGI'),
    ('MARAVILHA', 'MARAVILHA'),
    ('MARECHAL', 'MARECHAL DEODORO'),
    ('MARIBONDO', 'MARIBONDO'),
    ('MATA', 'MATA GRANDE'),
    ('MATRIZ', 'MATRIZ DE CAMARAGIBE'),
    ('MESSIAS', 'MESSIAS'),
    ('MINADOR', 'MINADOR DO NEGRÃO'),
    ('MONTEIROPOLIS', 'MONTEIRÓPOLIS'),
    ('MURICI', 'MURICI'),
    ('NOVO', 'NOVO LINO'),
    ('ODAFLORES', 'OLHO D’ÁGUA DAS FLÔRES'),
    ('ODACASADO', 'OLHO D’ÁGUA DO CASADO'),
    ('ODAGRANDE', 'OLHO D’ÁGUA GRANDE'),
    ('OLIVENCA', 'OLIVENÇA'),
    ('OURO', 'OURO BRANCO'),
    ('PALESTINA', 'PALESTINA'),
    ('PALMEIRA', 'PALMEIRA DOS ÍNDIOS'),
    ('PAO', 'PÃO DE AÇUCAR'),
    ('PARICONHA', 'PARICONHA'),
    ('PARIPUEIRA', 'PARIPUEIRA'),
    ('PASSO', 'PASSO DE CAMARAGIBE'),
    ('PAULO', 'PAULO JACINTO'),
    ('PENEDO', 'PENEDO'),
    ('PIACABUCU', 'PIAÇABUÇU'),
    ('PILAR', 'PILAR'),
    ('PINDOBA', 'PINDOBA'),
    ('PIRANHAS', 'PIRANHAS'),
    ('POCO', 'POÇO DAS TRINCHEIRAS'),
    ('PCALVO', 'PORTO CALVO'),
    ('PPEDRAS', 'PORTO DE PEDRAS'),
    ('PRCOLEGIO', 'PORTO REAL DO COLÉGIO'),
    ('QUEBRANGULO', 'QUEBRANGULO'),
    ('RIO', 'RIO LARGO'),
    ('ROTEIRO', 'ROTEIRO'),
    ('SANTA', 'SANTA LUZIA DO NORTE'),
    ('SANTANAIP', 'SANTANA DO IPANEMA'),
    ('SANTANAMUN', 'SANTANA DO MUNDAÚ'),
    ('SBRAS', 'SÃO BRÁS'),
    ('SJLAJE', 'SÃO JOSÉ DA LAJE'),
    ('SJTAPERA', 'SÃO JOSÉ DA TAPERA'),
    ('SLQUITUNDE', 'SÃO LUIZ DO QUITUNDE'),
    ('SMCAMPOS', 'SÃO MIGUEL DOS CAMPOS'),
    ('SMMILAGRES', 'SÃO MIGUEL DOS MILAGRES'),
    ('SSEBASTIAO', 'SÃO SEBASTIÃO'),
    ('SATUBA', 'SATUBA'),
    ('SENADOR', 'SENADOR RUI PALMEIRA'),
    ('TANQUE', 'TANQUE D’ARCA'),
    ('TAQUARANA', 'TAQUARANA'),
    ('TEOTONIO', 'TEOTÔNIO VILELA'),
    ('TRAIPU', 'TRAIPU')
)
