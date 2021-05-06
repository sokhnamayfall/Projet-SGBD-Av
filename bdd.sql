

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
--

-- --------------------------------------------------------

--
-- Structure de la table `commune`
--

CREATE TABLE `commune` (
  `id` int(11) NOT NULL,
  `nom_localite` varchar(70) NOT NULL,
  `shape_length` varchar(60) NOT NULL,
  `shape_area` varchar(60) NOT NULL,
  `depart_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `commune`
--

INSERT INTO `commune` (`id`, `nom_localite`, `shape_length`, `shape_area`, `depart_id`) VALUES
(21, 'Kiniéba', '3,44974106385052', '0,289777610059463', 36),
(22, 'Moudéri', '1,85321402696629', '0,115418937836212', 36),
(23, 'Bellé', '2,13671439625322', '0,156320700090821', 36),
(24, 'lambaye', '0,815746346909388', '0,0390028785323814', 5),
(25, 'ngoye', '0,994643166349243', '0,0390837835875476', 5),
(26, 'baba garage', '0,814006184987481', '0,0339509623077762', 5),
(27, 'kataba1', '2,2840076852327', '0,157732221525296', 43),
(28, 'tangori', '1,53100412476116', '0,088389240380688', 43),
(29, 'tendouk', '1,58977987955449', '0,0748259240193464', 43),
(30, 'sindian', '1,93122583374522', '0,122453697797066', 43),
(31, 'mabo', '1,11647640900353', '0,0522439976294484', 11),
(32, 'keur mboucki', '0,838270559639596', '0,0440615601699853', 11),
(33, 'bona', '1,53114667732862', '0,0673058127306629', 33),
(34, 'bogal', '1,74450445402789', '0,105096220191511', 33),
(35, 'diaroume', '1,73955048095842', '0,0662382423299621', 33),
(36, 'ndiaye', '2,66681693064985', '0,26001563230616', 30),
(37, 'mbane', '2,17105157612957', '0,183575650978069', 30),
(38, 'parcelles assainies', '0,185066297950443', '0,00129977662871017', 1),
(39, 'grand dakar', '0,293069667218234', '0,00159009711806086', 1),
(40, 'ndoulo', '1,01419813865762', '0,0543432135354443', 6),
(41, 'ndindy', '1,01848100476449', '0,0538064890119523', 6),
(42, 'diakhao', '1,61848880036918', '0,0538726529275798', 8),
(43, 'fimla', '1,62607240375744', '0,0870719180151116', 8),
(44, 'tataguine', '1,03623105414263', '0,0445821302652438', 8),
(45, 'niakhar', '0,871201551751873', '0,0345832830556731', 8),
(46, 'djilor', '1,25164393823024', '0,0732264997478594', 10),
(47, 'toubacouta', '1,76027698462562', '0,120316280283208', 10),
(48, 'niodior', '1,13367757411186', '0,0545820096806829', 10),
(49, 'colobane', '1,485541847424', '0,0783401569032701', 9),
(50, 'ouadiour', '0,915387006261776', '0,0435385490327076', 9),
(51, 'dianke mankan', '3,24804152312199', '0,253871998270137', 37),
(52, 'koulor', '3,6651037816389', '0,567670319929168', 37),
(53, 'bala', '2,45507230266764', '0,23554677649879', 37),
(54, 'bouinguel bamba', '2,21522136536286', '0,25287368167686', 37),
(55, 'simbandi brassou', '1,08929173599929', '0,0445000470078753', 34),
(56, 'djibanar', '1,40655980691542', '0,0610787063429435', 34),
(57, 'karantaba', '1,06895050968843', '0,0388500118079362', 34),
(58, 'guediawaye', '0,211543734703812', '0,00118575017013006', 4),
(59, 'mbadakhoune', '0,00118575017013006', '0,0456687632093817', 46),
(60, 'nguelou', '1,42152996246746', '0,0449821656104678', 46),
(61, 'gniby', '1,54445569143051', '0,119661569368707', 16),
(62, 'katakel', '1,64956862220059', '0,10309743992664', 16),
(63, 'sinthiou', '3,84345190191716', '0,514992311627128', 28),
(64, 'orkadiere', '2,55516249720208', '0,215329060260977', 28),
(65, 'sibassor/ngothie', '1,0566218553614', '0,0377625323039112', 15),
(66, 'koumbal', '1,53951633297828', '0,0683722322983824', 15),
(67, 'ndiedieng', '1,23051675648968', '0,0513500403371598', 15),
(68, 'ndande', '1,59545386828287', '0,128459741881643', 26),
(69, 'darou mousty', '1,55842648069792', '0,136071436752193', 26),
(70, 'sagatta gueth', '1,3825040574549', '0,0693409679170729', 26),
(71, 'bandafassi', '5,04843808726331', '0,479630780542433', 18),
(72, 'fongolemi', '1,59047272031547', '0,10864473248176', 18),
(73, 'mampatim', '2,56980299971972', '0,203934484611503', 21),
(74, 'sare bidji', '0,957786349923618', '0,0479397464645209', 21),
(75, 'dioulakolon', '1,0194153181417', '0,0460348484005111', 21),
(76, 'koutiaba wolof', '3,02055804244959', '0,423574970726257', 38),
(77, 'bamba tialene', '1,84646023570224', '0,153030525979567', 38),
(78, 'missira wadene', '2,19742294045623', '0,182193448147021', 13),
(79, 'ida mouride', '1,77663535836572', '0,103265514361719', 13),
(80, 'lour escale', '1,47778831694412', '0,0945352919506427', 13),
(81, 'yang yang ', '2,73526157792311', '0,372823632918683', 25),
(82, 'sagata wolof', '2,02216231350453', '0,245698883114293', 25),
(83, 'barkedji', '3,37539295125872', '0,514385450048084', 25),
(84, 'dodji', '2,51851329712743', '0,215439425151021', 25),
(85, 'keur momar sarr', '2,13576724447709', '0,238674605053873', 24),
(86, 'koki', '1,15366843602716', '0,0757526877364267', 24),
(87, 'mbediene', '1,04140575878344', '0,0634347768656937', 24),
(88, 'sakal', '1,55589624373375', '0,100268700491278', 24),
(89, 'darou minam 2', '1,59575602583206', '0,136736768926831', 14),
(90, 'sagna', '1,22986509485721', '0,0892854265798246', 14),
(91, 'ogo', '3,37830955431895', '0,326065399467664', 27),
(92, 'agname civol', '1,92093942177388', '0,159111012199733', 27),
(93, 'ndame', '1,26653780923747', '0,0809696336542601', 7),
(94, 'taif', '0,966776039912594', '0,048767532212149', 7),
(95, 'kael', '1,15612374241271', '0,0582211787760598', 7),
(96, 'fissel', '0,916626720113', '0,0412987918634306', 40),
(97, 'sessene', '1,52905040997', '0,916626720113', 40),
(98, 'sindia', '1,28344601614', '0,0601760296763748', 40),
(99, 'ndoma', '2,27045596615712', '0,178487908889519', 22),
(100, 'nianing', '1,97248421690099', '0,139587361534306', 22),
(101, 'fafacourou', '1,24371772057919', '0,0743952444783047', 22),
(102, 'paoscoto', '1,33900869219813', '0,0848670582284041', 17),
(103, 'wak ngouna', '1,21368226862553', '0,0570883524859484', 17),
(104, 'medina sabakh', '1,04212083450399', '0,0502442639705659', 17),
(105, 'loudi wolof', '0,980370796792375', '0,0389789345088344', 44),
(106, 'cabrousse', '1,22168253615654', '0,0350199398754446', 44),
(107, 'niayes', '0,276567032789609', '0,00353595137147245', 2),
(108, 'thiaroye', '0,266268929892834', '0,00260547471733351', 2),
(109, 'pikine dagoudane', '0,175899234214239', '0,00123487267576803', 2),
(114, 'gamadji sarre', '3,63952084115707', '0,326713217819182', 31),
(115, 'thille boubacar', '2,38568979706152', '0,270774889785287', 31),
(116, 'salde', '2,56240158358857', '0,231546445868218', 31),
(117, 'cas-cas', '2,47878881436149', '0,262867289950219', 31),
(118, 'velinguara', '5,98400451497421', '1,21115390384295', 29),
(119, 'sangalkam', '0,789174032911314', '0,0287096238854376', 3),
(120, 'bargny', '0,206870642908284', '0,00154588227026498', 3),
(121, 'rao', '1,35968308821127', '0,0678552413013982', 32),
(122, 'dar salam', '1,92099713888779', '0,0981872124456905', 19),
(123, 'daketeli', '1,5426363128624', '0,0613830512288253', 19),
(124, 'sabadola', '3,45268277741905', '0,351607689518536', 20),
(125, 'bembou', '3,58800400927838', '0,299071523441307', 20),
(126, 'diende', '1,84728133178092', '0,115439644074636', 35),
(127, 'djibabouya', '1,26234243691562', '0,0566877203777382', 35),
(128, 'djiredji', '1,31820842184418', '0,0567183372860827', 35),
(129, 'missira', '7,49172487201982', '0,705111818750314', 39),
(130, 'makacoulibantang', '1,95870721192735', '0,147424566518414', 39),
(131, 'koussanar', '2,87835866022301', '0,263876924679808', 39),
(132, 'keur moussa', '1,1668527818546', '0,0479672991968752', 41),
(133, 'thienaba', '0,917387654496461', '0,0453318262489715', 41),
(134, 'noto', '0,908561998287087', '0,0416188849338219', 41),
(135, 'niakhene', '1,54583073853667', '0,0657205398254939', 42),
(136, 'pambal', '1,28485593615824', '0,0570751151623885', 42),
(137, 'meouane', '1,2847965597102', '0,0824150383099563', 42),
(138, 'merina dakhar', '1,19967242877881', '0,0541322397987701', 42),
(139, 'bonconto', '3,45809748129816', '0,238051708713576', 23),
(140, 'pakour', '2,12298367871657', '0,100059284155729', 23),
(141, 'sare coly sarre', '1,94946880940019', '0,115481517398157', 23),
(142, 'niaguis', '1,24983355088007', '0,0580569496926675', 45),
(143, 'niassia', '1,03610091653735', '0,0368654089576011', 45),
(144, 'almadies', '0,331860648401936', '0,00266070231322952', 1),
(145, 'plateau', '0,268454893273306', '0,00129852087521626', 1);

-- --------------------------------------------------------

--
-- Structure de la table `departement`
--

CREATE TABLE `departement` (
  `id` int(11) NOT NULL,
  `nom_localite` varchar(70) NOT NULL,
  `region_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `departement`
--

INSERT INTO `departement` (`id`, `nom_localite`, `region_id`) VALUES
(1, 'dakar', 1),
(2, 'pikine', 1),
(3, 'rufisque', 1),
(4, 'guediawaye', 1),
(5, 'bambeye', 2),
(6, 'diourbel', 2),
(7, 'mbacke', 2),
(8, 'fatick', 3),
(9, 'gossas', 3),
(10, 'foundiougne', 3),
(11, 'birkelane', 4),
(12, 'kaffrine', 4),
(13, 'koungheul', 4),
(14, 'malem-hodar', 4),
(15, 'kaolack', 5),
(16, 'kaffrine', 5),
(17, 'nioro du rip', 5),
(18, 'kedougou', 6),
(19, 'salemata', 6),
(20, 'saraya', 6),
(21, 'kolda', 7),
(22, 'medina yoro foulah', 7),
(23, 'velingara', 7),
(24, 'louga', 8),
(25, 'linguere', 8),
(26, 'kebemer', 8),
(27, 'matam', 9),
(28, 'kanel', 9),
(29, 'ranerou-ferlo', 9),
(30, 'dagana', 10),
(31, 'podor', 10),
(32, 'saint-louis', 10),
(33, 'bounkiling', 11),
(34, 'goudomp', 11),
(35, 'sedhiou', 11),
(36, 'bakel', 12),
(37, 'goudiry', 12),
(38, 'koumpentoum', 12),
(39, 'tambacounda', 12),
(40, 'mbour', 13),
(41, 'thies', 13),
(42, 'tivaoune', 13),
(43, 'bignona', 14),
(44, 'oussouye', 14),
(45, 'ziguinchor', 14),
(46, 'guinguineo', 5);

-- --------------------------------------------------------

--
-- Structure de la table `details_cas`
--

CREATE TABLE `fichier` (
  `id` int(11) PRIMARY KEY AUTO_INCREMENT,
  `nbre_positifs` int(11) NOT NULL,
  `nbre_cas_contact` int(11) ,
  `nbre_cas_communautaires` int(11) ,
  `nbre_gueris` int(11) ,
  `nbre_deces` int(11) ,
  `nbre_test` int(11) ,
  `nbre_cas_importes` int(11) ,
  `nbre_cas_graves` int(11) ,
  `nom_fichier_source` varchar(70) ,
  `nbre_vaccines` varchar(70) ,
  `date_communique` varchar(20) ,
  `num_communique` int 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `details_cas_communes`
--

CREATE TABLE `casCommunes` (
  `id` int(11) NOT NULL,
  `nbre_nouv_cas` int(11) NOT NULL,
  `nom_fichier_source` varchar(70) NOT NULL,
  `date_communique` date NOT NULL,
  `date` date NOT NULL,
  `commune_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `details_cas_departements`
--

CREATE TABLE `casDepartements` (
  `id` int(11) NOT NULL,
  `nbre_nouv_cas` int(11) NOT NULL,
  `nom_fichier_source` varchar(70) NOT NULL,
  `date_communique` date NOT NULL,
  `departement_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `details_cas_regions`
--

CREATE TABLE `casRegions` (
  `id` int(11) NOT NULL,
  `nbre_nouv_cas` int(11) NOT NULL,
  `nom_fichier_source` varchar(70) NOT NULL,
  `date_communique` date NOT NULL,
  `region_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `region`
--

CREATE TABLE `region` (
  `id` int(11) NOT NULL,
  `nom_localite` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `region`
--

INSERT INTO `region` (`id`, `nom_localite`) VALUES
(1, 'dakar'),
(2, 'diourbel'),
(3, 'fatick'),
(4, 'kaffrine'),
(5, 'kaolack'),
(6, 'kedougou'),
(7, 'kolda'),
(8, 'louga'),
(9, 'matam'),
(10, 'saint-louis'),
(11, 'sedhiou'),
(12, 'tambacounda'),
(13, 'thies'),
(14, 'ziguinchor');

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(70) NOT NULL,
  `password` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `commune`
--
ALTER TABLE `commune`
  ADD PRIMARY KEY (`id`),
  ADD KEY `depart_id` (`depart_id`);

--
-- Index pour la table `departement`
--
ALTER TABLE `departement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `region_id` (`region_id`);

--
-- Index pour la table `details_cas`
--
ALTER TABLE `fichier`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `details_cas_communes`
--
ALTER TABLE `casCommunes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `commune_id` (`commune_id`);

--
-- Index pour la table `details_cas_departements`
--
ALTER TABLE `casDepartements`
  ADD PRIMARY KEY (`id`),
  ADD KEY `departement_id` (`departement_id`);

--
-- Index pour la table `details_cas_regions`
--
ALTER TABLE `casRegions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `region_id` (`region_id`);

--
-- Index pour la table `region`
--
ALTER TABLE `region`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `commune`
--
ALTER TABLE `commune`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=148;

--
-- AUTO_INCREMENT pour la table `departement`
--
ALTER TABLE `departement`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT pour la table `details_cas`
--
ALTER TABLE `fichier`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `details_cas_communes`
--
ALTER TABLE `casCommunes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `details_cas_departements`
--
ALTER TABLE `casDepartements`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `details_cas_regions`
--
ALTER TABLE `casRegions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `region`
--
ALTER TABLE `region`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT pour la table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `commune`
--
ALTER TABLE `commune`
  ADD CONSTRAINT `commune_ibfk_1` FOREIGN KEY (`depart_id`) REFERENCES `departement` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `departement`
--
ALTER TABLE `departement`
  ADD CONSTRAINT `departement_ibfk_1` FOREIGN KEY (`region_id`) REFERENCES `region` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `details_cas_communes`
--
ALTER TABLE `casCommunes`
  ADD CONSTRAINT `casCommunes_ibfk_1` FOREIGN KEY (`commune_id`) REFERENCES `commune` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `details_cas_departements`
--
ALTER TABLE `casDepartements`
  ADD CONSTRAINT `casDepartements_ibfk_1` FOREIGN KEY (`departement_id`) REFERENCES `departement` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `details_cas_regions`
--
ALTER TABLE `casRegions`
  ADD CONSTRAINT `casRegions_ibfk_1` FOREIGN KEY (`region_id`) REFERENCES `region` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
