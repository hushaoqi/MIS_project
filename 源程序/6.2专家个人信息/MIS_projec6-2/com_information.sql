/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : com_information

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2018-08-10 21:45:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `information`
-- ----------------------------
DROP TABLE IF EXISTS `information`;
CREATE TABLE `information` (
  `commodityCode` char(6) NOT NULL,
  `commodityName` char(12) DEFAULT NULL,
  `specification` char(8) DEFAULT NULL,
  `chargeUnit` char(6) DEFAULT NULL,
  `unitPrice` float(8,2) DEFAULT NULL,
  `outputCode` char(8) DEFAULT NULL,
  PRIMARY KEY (`commodityCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of information
-- ----------------------------
INSERT INTO `information` VALUES ('15455', '鼠标', '电子', '件', '2.00', '154552');
INSERT INTO `information` VALUES ('15485', '香蕉', '水果', '千克', '5.80', '154853');
INSERT INTO `information` VALUES ('15648', '电脑', '电子产品', '台', '5966.00', '156488');
INSERT INTO `information` VALUES ('16548', '土豆', '蔬菜', '千克', '3.00', '165487');
INSERT INTO `information` VALUES ('28444', 'Python编程', '书', '本', '39.23', '284440');
INSERT INTO `information` VALUES ('46551', '棉被', '衣物', '件', '258.00', '465511');
INSERT INTO `information` VALUES ('46578', '西红柿', '蔬菜', '千克', '8.70', '465780');
INSERT INTO `information` VALUES ('46884', '白菜', '蔬菜', '千克', '3.00', '468844');
INSERT INTO `information` VALUES ('48694', '辣条', '休闲食品', '袋', '2.00', '486946');
INSERT INTO `information` VALUES ('48848', '鸡蛋', '食物', '个', '6.00', '488481');
INSERT INTO `information` VALUES ('48954', '篮球', '体育用品', '个', '108.00', '489540');
INSERT INTO `information` VALUES ('48984', '键盘', '电子', '件', '45.00', '489840');
INSERT INTO `information` VALUES ('49845', '手机', '电子', '件', '4898.00', '498450');
INSERT INTO `information` VALUES ('58948', '西瓜', '水果', '千克', '2.30', '589485');
INSERT INTO `information` VALUES ('58952', '西红柿', '水果', '千克', '6.00', '589521');

-- ----------------------------
-- Table structure for `professors`
-- ----------------------------
DROP TABLE IF EXISTS `professors`;
CREATE TABLE `professors` (
  `name` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `EngName` char(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `country` char(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `sex` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `nation` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `IDtype` char(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ID` char(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `birthdate` char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `isAcademicia` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `isDocent` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `jobTitle` char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `education` char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `degree` char(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `schoolTag` char(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `graduateYear` char(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `major` char(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of professors
-- ----------------------------
INSERT INTO `professors` VALUES ('胡绍齐', 'hhh', '中国', '男', '汉族', '身份证', '145645887554555555', '199611', '两院院士', '是', '正高级', '研究生', '博士', '大连理工大学', '2020', '软件工程');
INSERT INTO `professors` VALUES ('鹿晗', 'luhan', '中国', '女', '汉族', '身份证', '456464854648484854', '199110', '科学院院士', '是', '副高级', '研究生', '硕士', '中央戏剧学院', '1996', '表演');
INSERT INTO `professors` VALUES ('吴亦凡', 'fanMrwu', '中国', '男', '汉族', '身份证', '787946548545645586', '199002', '否', '否', '其他', '其他', '其他', '中国音乐学院', '1996', '唱歌');
