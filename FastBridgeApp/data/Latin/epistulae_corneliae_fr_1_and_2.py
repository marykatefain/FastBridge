import text
nan=""
section_words = {'start': -1, '1': 47, '2': 244, 'end': -2}
the_text =  [('DICO/2', 0, 'Dices', '', '', '1', 1), ('PVLCHER', 1, 'pulchrum', '', '', '1', 2), ('SVM/1', 2, 'esse', '', '', '1', 7), ('INIMICVS/2', 3, 'inimicos', '', '', '1', 3), ('VLCISCOR', 4, 'ulcisci', '', '', '1', 1), ('IS', 5, 'Id', '', '', '1', 12), ('NEQVE', 6, 'neque', '', '', '1', 3), ('MAIOR', 7, 'maius', '', '', '1', 2), ('NEQVE', 8, 'neque', '', '', '1', 3), ('PVLCHER', 9, 'pulchrius', '', '', '1', 2), ('QVISQVAM', 10, 'cuiquam', '', '', '1', 2), ('ATQVE/1', 11, 'atque', '', '', '1', 8), ('EGO', 12, 'mihi', '', '', '1', 9), ('SVM/1', 13, 'esse', '', '', '1', 7), ('VIDEO', 14, 'uidetur', '', '', '1', 1), ('SED', 15, 'sed', '', '', '1', 3), ('SI/2', 16, 'si', '', '', '1', 3), ('LICEO', 17, 'liceat', '', '', '1', 1), ('RESPVBLICA', 18, 're PUBLICA', '', '', '1', 4), ('SALVVS', 19, 'salua', '', '', '1', 1), ('IS', 20, 'ea', '', '', '1', 12), ('PERSEQVOR', 21, 'persequi', '', '', '1', 1), ('SED', 22, 'Sed', '', '', '1', 3), ('QVATENVS/1', 23, 'quatenus', '', '', '1', 1), ('IS', 24, 'id', '', '', '1', 12), ('FIO', 25, 'fieri', '', '', '1', 2), ('NON', 26, 'non', '', '', '1', 5), ('POSSVM/1', 27, 'potest', '', '', '1', 5), ('MVLTVS', 28, 'multo', '', '', '1', 2), ('TEMPVS/1', 29, 'tempore', '', '', '1', 3), ('MVLTVS', 30, 'multis', '', '', '1', 2), ('QVE', 31, 'que', '', '', '1', 2), ('PARS', 32, 'partibus', '', '', '1', 3), ('INIMICVS/2', 33, 'inimici', '', '', '1', 3), ('NOSTER', 34, 'nostri', '', '', '1', 2), ('NON', 35, 'non', '', '', '1', 5), ('PEREO/1', 36, 'peribunt', '', '', '1', 2), ('ATQVE/1', 37, 'atque', '', '', '1', 8), ('VT/4', 38, 'uti', '', '', '1', 4), ('NVNC', 39, 'nunc', '', '', '1', 1), ('SVM/1', 40, 'sunt', '', '', '1', 7), ('SVM/1', 41, 'erunt', '', '', '1', 7), ('POTIS', 42, 'potius', '', '', '1', 1), ('QVAM/1', 43, 'quam', '', '', '1', 2), ('RESPVBLICA', 44, 'RES PUBLICA', '', '', '1', 4), ('PROFLIGO', 45, 'profligetur', '', '', '1', 2), ('ATQVE/1', 46, 'atque', '', '', '1', 8), ('PEREO/1', 47, 'pereat', '', '', '1', 2), ('VERBVM', 48, 'Uerbis', '', '', '2', 1), ('CONCIPIO', 49, 'conceptis', '', '', '2', 1), ('DEIERO', 50, 'deierare', '', '', '2', 1), ('AVDEO', 51, 'ausim', '', '', '2', 1), ('PRAETERQVAM', 52, 'praeterquam', '', '', '2', 1), ('QVI/1', 53, 'qui', '', '', '2', 7), ('TIBERIVS/N', 54, 'Tiberium', '', '', '2', 1), ('GRACCHVS/N', 55, 'Gracchum', '', '', '2', 1), ('NECO', 56, 'necarunt', '', '', '2', 1), ('NEMO', 57, 'neminem', '', '', '2', 1), ('INIMICVS/2', 58, 'inimicum', '', '', '2', 3), ('TANTVS', 59, 'tantum', '', '', '2', 4), ('MOLESTIA', 60, 'molestiae', '', '', '2', 2), ('TANTVS', 61, 'tantum', '', '', '2', 4), ('QVE', 62, 'que', '', '', '2', 2), ('LABOR/1', 63, 'laboris', '', '', '2', 2), ('QVANTVS/1', 64, 'quantum', '', '', '2', 1), ('TV', 65, 'te', '', '', '2', 6), ('OB', 66, 'ob', '', '', '2', 1), ('HIC/1', 67, 'has', '', '', '2', 1), ('RES', 68, 'res', '', '', '2', 3), ('EGO', 69, 'mihi', '', '', '2', 9), ('TRADO', 70, 'tradidisse', '', '', '2', 1), ('QVI/1', 71, 'quem', '', '', '2', 7), ('OPORTET', 72, 'oportebat', '', '', '2', 1), ('OMNIS', 73, 'omnium', '', '', '2', 2), ('IS', 74, 'eorum', '', '', '2', 12), ('QVI/1', 75, 'quos', '', '', '2', 7), ('ANTEHAC', 76, 'antehac', '', '', '2', 1), ('HABEO', 77, 'habui', '', '', '2', 6), ('LIBER/2', 78, 'liberos', '', '', '2', 1), ('PARS', 79, 'partis', '', '', '2', 3), ('IS', 80, 'eorum', '', '', '2', 12), ('TOLERO', 81, 'tolerare', '', '', '2', 1), ('ATQVE/1', 82, 'atque', '', '', '2', 8), ('CVRO', 83, 'curare', '', '', '2', 1), ('VT/4', 84, 'ut', '', '', '2', 4), ('QVAM/1', 85, 'quam', '', '', '2', 2), ('MINIMVS', 86, 'minimum', '', '', '2', 1), ('SOLLICITVDO', 87, 'sollicitudinis', '', '', '2', 1), ('IN', 88, 'in', '', '', '2', 5), ('SENECTA', 89, 'senecta', '', '', '2', 1), ('HABEO', 90, 'haberem', '', '', '2', 6), ('VTIQVE', 91, 'utique', '', '', '2', 1), ('QVICVMQVE/1', 92, 'quaecumque', '', '', '2', 1), ('AGO', 93, 'ageres', '', '', '2', 1), ('IS', 94, 'ea', '', '', '2', 12), ('VOLO/3', 95, 'uelles', '', '', '2', 1), ('MAXIME', 96, 'maxime', '', '', '2', 1), ('EGO', 97, 'mihi', '', '', '2', 9), ('PLACEO', 98, 'placere', '', '', '2', 2), ('ATQVE/1', 99, 'atque', '', '', '2', 8), ('VT/4', 100, 'uti', '', '', '2', 4), ('NEFAS', 101, 'nefas', '', '', '2', 1), ('HABEO', 102, 'haberes', '', '', '2', 6), ('RES', 103, 'rerum', '', '', '2', 3), ('MAIOR', 104, 'maiorum', '', '', '2', 2), ('ADVERSVS/2', 105, 'aduersum', '', '', '2', 1), ('MEVS', 106, 'meam', '', '', '2', 1), ('SENTENTIA', 107, 'sententiam', '', '', '2', 1), ('QVISQVAM', 108, 'quicquam', '', '', '2', 2), ('FACIO', 109, 'facere', '', '', '2', 2), ('PRAESERTIM', 110, 'praesertim', '', '', '2', 1), ('EGO', 111, 'mihi', '', '', '2', 9), ('QVI/1', 112, 'cui', '', '', '2', 7), ('PARVVS/2', 113, 'parua', '', '', '2', 1), ('PARS', 114, 'pars', '', '', '2', 3), ('VITA', 115, 'uitae', '', '', '2', 2), ('SVPERSVM/1', 116, 'superest', '', '', '2', 1), ('NEQVIDEM', 117, 'Ne', '', '', '2', 2), ('IS', 118, 'id', '', '', '2', 12), ('NEQVIDEM', 119, 'quidem', '', '', '2', 2), ('TAM', 120, 'tam', '', '', '2', 1), ('BREVIS', 121, 'breue', '', '', '2', 1), ('SPATIVM', 122, 'spatium', '', '', '2', 1), ('POSSVM/1', 123, 'potest', '', '', '2', 5), ('OPITVLOR', 124, 'opitulari', '', '', '2', 1), ('QVIN/1', 125, 'quin', '', '', '2', 1), ('ET/2', 126, 'et', '', '', '2', 6), ('EGO', 127, 'mihi', '', '', '2', 9), ('ADVERSO', 128, 'aduersere', '', '', '2', 1), ('ET/2', 129, 'et', '', '', '2', 6), ('RESPVBLICA', 130, 'rem PUBLICAM', '', '', '2', 4), ('PROFLIGO', 131, 'profliges', '', '', '2', 2), ('DENIQVE', 132, 'Denique', '', '', '2', 1), ('QVI/1', 133, 'quae', '', '', '2', 7), ('PAVSA', 134, 'pausa', '', '', '2', 1), ('SVM/1', 135, 'erit', '', '', '2', 7), ('ECQVANDO', 136, 'Ecquando', '', '', '2', 4), ('DESINO', 137, 'desinet', '', '', '2', 2), ('FAMILIA', 138, 'familia', '', '', '2', 1), ('NOSTER', 139, 'nostra', '', '', '2', 2), ('INSANIO', 140, 'insanire', '', '', '2', 1), ('ECQVANDO', 141, 'Ecquando', '', '', '2', 4), ('MODVS', 142, 'modus', '', '', '2', 1), ('IS', 143, 'ei', '', '', '2', 12), ('RES', 144, 'rei', '', '', '2', 3), ('HABEO', 145, 'haberi', '', '', '2', 6), ('POSSVM/1', 146, 'poterit', '', '', '2', 5), ('ECQVANDO', 147, 'Ecquando', '', '', '2', 4), ('DESINO', 148, 'desinemus', '', '', '2', 2), ('ET/2', 149, 'et', '', '', '2', 6), ('HABEO', 150, 'habentes', '', '', '2', 6), ('ET/2', 151, 'et', '', '', '2', 6), ('PRAEBEO', 152, 'praebentes', '', '', '2', 1), ('MOLESTIA', 153, 'molestiis', '', '', '2', 2), ('INSISTO', 154, 'insistere', '', '', '2', 1), ('ECQVANDO', 155, 'Ecquando', '', '', '2', 4), ('PERPVDESCO', 156, 'perpudescet', '', '', '2', 1), ('MISCEO', 157, 'miscenda', '', '', '2', 1), ('ATQVE/1', 158, 'atque', '', '', '2', 8), ('PERTVRBO/2', 159, 'perturbanda', '', '', '2', 1), ('RESPVBLICA', 160, 're pubLICA', '', '', '2', 4), ('SED', 161, 'Sed', '', '', '2', 3), ('SI/2', 162, 'si', '', '', '2', 3), ('OMNINO', 163, 'omnino', '', '', '2', 1), ('IS', 164, 'id', '', '', '2', 12), ('FIO', 165, 'fieri', '', '', '2', 2), ('NON', 166, 'non', '', '', '2', 5), ('POSSVM/1', 167, 'potest', '', '', '2', 5), ('VBI/1', 168, 'ubi', '', '', '2', 2), ('EGO', 169, 'ego', '', '', '2', 9), ('MORIOR', 170, 'mortua', '', '', '2', 2), ('SVM/1', 171, 'ero', '', '', '2', 7), ('PETO', 172, 'petito', '', '', '2', 1), ('TRIBVNATVS', 173, 'tribunatum', '', '', '2', 1), ('PER', 174, 'per', '', '', '2', 1), ('EGO', 175, 'me', '', '', '2', 9), ('FACIO', 176, 'facito', '', '', '2', 2), ('QVI/1', 177, 'quod', '', '', '2', 7), ('LIBET', 178, 'lubebit', '', '', '2', 1), ('CVM/3', 179, 'cum', '', '', '2', 1), ('EGO', 180, 'ego', '', '', '2', 9), ('NON', 181, 'non', '', '', '2', 5), ('SENTIO', 182, 'sentiam', '', '', '2', 1), ('VBI/1', 183, 'Ubi', '', '', '2', 2), ('MORIOR', 184, 'mortua', '', '', '2', 2), ('SVM/1', 185, 'ero', '', '', '2', 7), ('PARENTO', 186, 'parentabis', '', '', '2', 1), ('EGO', 187, 'mihi', '', '', '2', 9), ('ET/2', 188, 'et', '', '', '2', 6), ('INVOCO', 189, 'inuocabis', '', '', '2', 1), ('DEVS', 190, 'deum', '', '', '2', 2), ('PARENS/1', 191, 'parentem', '', '', '2', 1), ('IN', 192, 'In', '', '', '2', 5), ('IS', 193, 'eo', '', '', '2', 12), ('TEMPVS/1', 194, 'tempore', '', '', '2', 3), ('NON', 195, 'non', '', '', '2', 5), ('PVDEO', 196, 'pudet', '', '', '2', 1), ('TV', 197, 'te', '', '', '2', 6), ('IS', 198, 'eorum', '', '', '2', 12), ('DEVS', 199, 'deum', '', '', '2', 2), ('PREX', 200, 'preces', '', '', '2', 1), ('EXPETO', 201, 'expetere', '', '', '2', 1), ('QVI/1', 202, 'quos', '', '', '2', 7), ('VIVVS/2', 203, 'uiuos', '', '', '2', 1), ('ATQVE/1', 204, 'atque', '', '', '2', 8), ('PRAESENS', 205, 'praesentes', '', '', '2', 1), ('RELINQVO', 206, 'relictos', '', '', '2', 1), ('ATQVE/1', 207, 'atque', '', '', '2', 8), ('DESERTVS', 208, 'desertos', '', '', '2', 1), ('HABEO', 209, 'habueris', '', '', '2', 6), ('NE/4', 210, 'Ne', '', '', '2', 2), ('ILLE', 211, 'ille', '', '', '2', 1), ('SINO', 212, 'sirit', '', '', '2', 1), ('IVPPITER/N', 213, 'Iuppiter', '', '', '2', 1), ('TV', 214, 'te', '', '', '2', 6), ('IS', 215, 'ea', '', '', '2', 12), ('PERSEVERO', 216, 'perseuerare', '', '', '2', 2), ('NEQVE', 217, 'nec', '', '', '2', 3), ('TV', 218, 'tibi', '', '', '2', 6), ('TANTVS', 219, 'tantam', '', '', '2', 4), ('DEMENTIA', 220, 'dementiam', '', '', '2', 1), ('VENIO', 221, 'uenire', '', '', '2', 1), ('IN', 222, 'in', '', '', '2', 5), ('ANIMVS', 223, 'animum', '', '', '2', 1), ('ET/2', 224, 'Et', '', '', '2', 6), ('SI/2', 225, 'si', '', '', '2', 3), ('PERSEVERO', 226, 'perseueras', '', '', '2', 2), ('VEREOR', 227, 'uereor', '', '', '2', 1), ('NE/4', 228, 'ne', '', '', '2', 2), ('IN', 229, 'in', '', '', '2', 5), ('OMNIS', 230, 'omnem', '', '', '2', 2), ('VITA', 231, 'uitam', '', '', '2', 2), ('TANTVS', 232, 'tantum', '', '', '2', 4), ('LABOR/1', 233, 'laboris', '', '', '2', 2), ('CVLPA', 234, 'culpa', '', '', '2', 1), ('TVVS', 235, 'tua', '', '', '2', 1), ('RECIPIO', 236, 'recipias', '', '', '2', 1), ('VT/4', 237, 'uti', '', '', '2', 4), ('IN', 238, 'in', '', '', '2', 5), ('NVLLVS', 239, 'nullo', '', '', '2', 1), ('TEMPVS/1', 240, 'tempore', '', '', '2', 3), ('TV', 241, 'tute', '', '', '2', 6), ('TV', 242, 'tibi', '', '', '2', 6), ('PLACEO', 243, 'placere', '', '', '2', 2), ('POSSVM/1', 244, 'possis', '', '', '2', 5)]
section_list ={'1': 'start', '2': '1', 'end': '2', 'start': 'start'}
title = "Epistulae Corneliae (fr. 1 and 2)"
section_level =  1
language = "Latin"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)