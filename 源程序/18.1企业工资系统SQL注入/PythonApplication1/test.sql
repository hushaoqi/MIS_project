/*
 Navicat MySQL Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80011
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 80011
 File Encoding         : 65001

 Date: 20/08/2018 14:29:54
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for salary_month
-- ----------------------------
DROP TABLE IF EXISTS `salary_month`;
CREATE TABLE `salary_month`  (
  `ID` char(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Month` int(6) NOT NULL,
  `Name` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Basic_salary` int(5) NULL DEFAULT NULL,
  `Bonus` int(5) NULL DEFAULT NULL,
  `Fine` int(5) NULL DEFAULT NULL,
  `True_salary` int(8) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`, `Month`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of salary_month
-- ----------------------------
INSERT INTO `salary_month` VALUES ('user', 201805, '张三', 5000, 3000, 400, 7600);
INSERT INTO `salary_month` VALUES ('user', 201806, '张三', 5000, 4000, 500, 8500);
INSERT INTO `salary_month` VALUES ('user', 201807, '张三', 5000, 4000, 400, 8600);

-- ----------------------------
-- Table structure for self_information
-- ----------------------------
DROP TABLE IF EXISTS `self_information`;
CREATE TABLE `self_information`  (
  `ID` char(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Name` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Sex` char(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Age` int(3) NULL DEFAULT NULL,
  `Hobbies` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of self_information
-- ----------------------------
INSERT INTO `self_information` VALUES ('user', '张三', '男', 32, '书法、羽毛球、');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `ID` char(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Password` char(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`ID`, `Password`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('user', 'user');

SET FOREIGN_KEY_CHECKS = 1;
