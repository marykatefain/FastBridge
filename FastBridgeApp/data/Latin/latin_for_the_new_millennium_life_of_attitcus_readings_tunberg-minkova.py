import text
nan=""
section_words = {'start': -1, '1': 14, '10': 26, '2': 39, '3': 52, '4': 65, '5': 80, '6': 94, '7': 109, '8': 124, '9': 139, 'end': -2}
the_text =  [('ADIVVO', 0, 'adiuvo', '', '', '1', 1), ('AMICVS/2', 1, 'amicus', '', '', '1', 1), ('CALAMITAS', 2, 'calamitas', '', '', '1', 1), ('COGNOSCO', 3, 'cognosco', '', '', '1', 1), ('DILIGENTIA', 4, 'diligentia', '', '', '1', 1), ('EMO', 5, 'emo', '', '', '1', 1), ('EXISTIMO', 6, 'existimo', '', '', '1', 1), ('FAMILIARIS/1', 7, 'familiaris', '', '', '1', 1), ('FAMILIARITAS', 8, 'familiaritas', '', '', '1', 1), ('GRATVS', 9, 'gratus', '', '', '1', 1), ('INTIMVS/2', 10, 'intimus', '', '', '1', 1), ('MEMOR', 11, 'memor', '', '', '1', 1), ('OPINIO', 12, 'opinio', '', '', '1', 1), ('PRAESTO/2', 13, 'praesto', '', '', '1', 1), ('TEGO', 14, 'tego', '', '', '1', 1), ('ACCEDO/1', 15, 'accedo', '', '', '10', 1), ('ADHIBEO', 16, 'adhibeo', '', '', '10', 1), ('COMPLEO', 17, 'compleo', '', '', '10', 1), ('CONSVLO', 18, 'consulo', '', '', '10', 1), ('CONTEMNO', 19, 'contemno', '', '', '10', 1), ('FEBRIS', 20, 'febris', '', '', '10', 1), ('INDIGEO', 21, 'indigeo', '', '', '10', 1), ('MORBVS', 22, 'morbus', '', '', '10', 1), ('RELIQVVMFACERE', 23, 'reliquum', '', '', '10', 1), ('RELIQVVS', 24, 'reliquus', '', '', '10', 1), ('TVEOR', 25, 'tueor', '', '', '10', 1), ('VALETVDO', 26, 'valetudo', '', '', '10', 1), ('ADVENTVS', 27, 'adventus', '', '', '2', 1), ('AVT', 28, 'aut', '', '', '2', 1), ('ETSI/2', 29, 'etsi', '', '', '2', 1), ('FORVM/1', 30, 'forum', '', '', '2', 1), ('HIEMS', 31, 'hiems', '', '', '2', 1), ('IMPERATOR', 32, 'imperator', '', '', '2', 1), ('INIMICVS/1', 33, 'inimicus', '', '', '2', 1), ('ITALIA/N', 34, 'Italia', '', '', '2', 1), ('MODOMODO', 35, 'modo', '', '', '2', 1), ('NVMERVS', 36, 'numerus', '', '', '2', 1), ('PRAESIDIVM', 37, 'praesidium', '', '', '2', 1), ('PRVDENTIA', 38, 'prudentia', '', '', '2', 1), ('SVMMVS', 39, 'summus', '', '', '2', 1), ('AFFLIGO', 40, 'affligo', '', '', '3', 1), ('BENEFICIVM', 41, 'beneficium', '', '', '3', 1), ('FLOREO', 42, 'floreo', '', '', '3', 1), ('IMMORTALIS', 43, 'immortalis', '', '', '3', 1), ('INIVRIA', 44, 'iniuria', '', '', '3', 1), ('LIBERALITAS', 45, 'liberalitas', '', '', '3', 1), ('MEMINI', 46, 'memini', '', '', '3', 1), ('NECESSARIVS/2', 47, 'necessarius', '', '', '3', 1), ('NEQVENEC', 48, 'neque', '', '', '3', 1), ('OBLIVISCOR', 49, 'obliviscor', '', '', '3', 1), ('PERCIPIO', 50, 'percipio', '', '', '3', 1), ('QVAM/1', 51, 'quam', '', '', '3', 1), ('TRIBVO', 52, 'tribuo', '', '', '3', 1), ('AVGEO', 53, 'augeo', '', '', '4', 1), ('CAESAR/N', 54, 'Caesar', '', '', '4', 1), ('CONDICIO', 55, 'condicio', '', '', '4', 1), ('CONIVNGO', 56, 'coniungo', '', '', '4', 1), ('CONSTITVO', 57, 'constituo', '', '', '4', 1), ('EFFICIO', 58, 'efficio', '', '', '4', 1), ('EQVES', 59, 'eques', '', '', '4', 1), ('GRATIA', 60, 'gratia', '', '', '4', 1), ('INCOMMODVM', 61, 'incommodum', '', '', '4', 1), ('NVPTIAE', 62, 'nuptiae', '', '', '4', 1), ('POTENTIA', 63, 'potentia', '', '', '4', 1), ('POTESTAS', 64, 'potestas', '', '', '4', 1), ('TANTVM/2', 65, 'tantum', '', '', '4', 1), ('AEDIFICIVM', 66, 'aedificium', '', '', '5', 1), ('ARTIFEX', 67, 'artifex', '', '', '5', 1), ('CETERVS', 68, 'ceterus', '', '', '5', 1), ('COGO', 69, 'cogo', '', '', '5', 1), ('COLLIS', 70, 'collis', '', '', '5', 1), ('CONSTO', 71, 'consto', '', '', '5', 1), ('ELEGANS', 72, 'elegans', '', '', '5', 1), ('HEREDITAS', 73, 'hereditas', '', '', '5', 1), ('LITTERATVS', 74, 'litteratus', '', '', '5', 1), ('MEDIOCRIS', 75, 'mediocris', '', '', '5', 1), ('NEQVIDEM', 76, 'quidem', '', '', '5', 1), ('PAR/2', 77, 'pār', '', '', '5', 1), ('SAL', 78, 'sal', '', '', '5', 1), ('SVMPTVS/1', 79, nan, '', '', '5', 1), ('TECTVM', 80, 'tectum', '', '', '5', 1), ('ALIQVIS', 81, 'aliquis', '', '', '6', 1), ('ARBITROR', 82, 'arbitror', '', '', '6', 1), ('CENO', 83, 'ceno', '', '', '6', 1), ('CONSVETVDO', 84, 'consuetudo', '', '', '6', 1), ('CONVIVIVM', 85, 'convivium', '', '', '6', 1), ('CVLTVS/1', 86, 'cultus', '', '', '6', 1), ('CVRA', 87, 'cura', '', '', '6', 1), ('HORTVS', 88, 'hortus', '', '', '6', 1), ('MENDACIVM', 89, 'mendacium', '', '', '6', 1), ('NAMQVE', 90, 'namque', '', '', '6', 1), ('NITOR/2', 91, 'nitor', '', '', '6', 1), ('POLLICEOR', 92, 'polliceor', '', '', '6', 1), ('PRAETER/2', 93, 'praeter', '', '', '6', 1), ('VTRVMAN', 94, 'utrum', '', '', '6', 1), ('ACCIDO/1', 95, 'accido', '', '', '7', 1), ('APPAREO', 96, 'appareo', '', '', '7', 1), ('APTVS', 97, 'aptus', '', '', '7', 1), ('CANO', 98, 'cano', '', '', '7', 1), ('DESIDERO', 99, 'desidero', '', '', '7', 1), ('EXTREMVS', 100, 'extremus', '', '', '7', 1), ('HVMANITAS', 101, 'humanitas', '', '', '7', 1), ('PRAECIPVE', 102, 'praecipue', '', '', '7', 1), ('PRINCEPS/1', 103, 'princeps', '', '', '7', 1), ('QVIDAM', 104, 'quidam', '', '', '7', 1), ('STVDIVM', 105, 'studium', '', '', '7', 1), ('TESTIMONIVM', 106, 'testimonium', '', '', '7', 1), ('VSQVE', 107, 'usque', '', '', '7', 1), ('VSVS', 108, 'usus', '', '', '7', 1), ('VVLGVS', 109, 'vulgus', '', '', '7', 1), ('ADEO/2', 110, 'adeo', '', '', '8', 1), ('AMPLIVS', 111, 'amplius', '', '', '8', 1), ('BREVIS', 112, 'brevis', '', '', '8', 1), ('DILIGENS', 113, 'diligens', '', '', '8', 1), ('EXPERS', 114, 'expers', '', '', '8', 1), ('ILLVSTRIS', 115, 'illustris', '', '', '8', 1), ('IMAGO', 116, 'imago', '', '', '8', 1), ('MAGISTRATVS', 117, 'magistratus', '', '', '8', 1), ('ORIGO', 118, 'origo', '', '', '8', 1), ('RESGESTAE', 119, 'res', '', '', '8', 1), ('SINGVLVS', 120, 'singuli', '', '', '8', 1), ('SVAVITAS', 121, 'suavitas', '', '', '8', 1), ('SVB', 122, 'sub', '', '', '8', 1), ('VERSVS/1', 123, 'versus', '', '', '8', 1), ('VOLVMEN', 124, 'volumen', '', '', '8', 1), ('AFFINITAS', 125, 'adfinitas', '', '', '9', 1), ('ANTIQVITAS', 126, 'antiquitas', '', '', '9', 1), ('CONSEQVOR', 127, 'consequor', '', '', '9', 1), ('FREQVENS', 128, 'frequens', '', '', '9', 1), ('FRVOR', 129, 'fruor', '', '', '9', 1), ('MOROR/1', 130, 'moror', '', '', '9', 1), ('NASCOR', 131, 'nascor', '', '', '9', 1), ('NECESSITVDO', 132, 'necessitudo', '', '', '9', 1), ('ORDO', 133, 'ordo', '', '', '9', 1), ('ORIOR', 134, 'orior', '', '', '9', 1), ('QVAMDIV/1', 135, 'quamdiu', '', '', '9', 1), ('QVIN/1', 136, 'quin', '', '', '9', 1), ('QVISQVAM', 137, 'quisquam', '', '', '9', 1), ('SANCIO', 138, 'sancio', '', '', '9', 1), ('VIRGO', 139, 'virgo', '', '', '9', 1)]
section_list ={'1': 'start', '10': '1', '2': '10', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', 'end': '9', 'start': 'start'}
title = "Latin for the New Millennium, Life of Attitcus Readings (Tunberg-Minkova)"
section_level =  1
language = "Latin"
book = text.Text(title, section_words, the_text, section_list, section_level, language, False, False)