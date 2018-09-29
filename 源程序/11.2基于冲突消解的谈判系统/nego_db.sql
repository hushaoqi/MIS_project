/*
 Navicat Premium Data Transfer

 Source Server         : root
 Source Server Type    : MySQL
 Source Server Version : 80011
 Source Host           : localhost:3306
 Source Schema         : nego_db

 Target Server Type    : MySQL
 Target Server Version : 80011
 File Encoding         : 65001

 Date: 20/07/2018 09:16:49
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for finally
-- ----------------------------
DROP TABLE IF EXISTS `finally`;
CREATE TABLE `finally`  (
  `unit_price_expect` int(4) NULL DEFAULT NULL COMMENT '商品单价',
  `unit_prices` int(4) NULL DEFAULT NULL COMMENT '购买费用合计',
  `profit_final` int(4) NULL DEFAULT NULL COMMENT '产品最终利润',
  `trans_profit_expect` int(4) NULL DEFAULT NULL COMMENT '运输费用单价',
  `total_cost_expect` int(4) NULL DEFAULT NULL COMMENT '原材料固定总费用期望值',
  `unit_cost_expect` int(4) NULL DEFAULT NULL COMMENT '原材料变动单位费用期望值',
  `trans_final` int(4) NULL DEFAULT NULL COMMENT '运输收入合计',
  `material_final` int(4) NULL DEFAULT NULL COMMENT '原料商收入',
  `id` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '主键',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of finally
-- ----------------------------
INSERT INTO `finally` VALUES (10, 200, 15, 4, 5, 5, 80, 105, '1');

-- ----------------------------
-- Table structure for product_dis
-- ----------------------------
DROP TABLE IF EXISTS `product_dis`;
CREATE TABLE `product_dis`  (
  `trans_id` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '运送单号',
  `p_sup_id` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '产品生产商编号',
  `p_pur_id` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '产品购买商编号',
  PRIMARY KEY (`trans_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of product_dis
-- ----------------------------
INSERT INTO `product_dis` VALUES ('1', 'A', 'B');

-- ----------------------------
-- Table structure for product_pur
-- ----------------------------
DROP TABLE IF EXISTS `product_pur`;
CREATE TABLE `product_pur`  (
  `Id` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '产品购买商编号',
  `pur_num` int(4) NOT NULL COMMENT '购买产品数量',
  `unit_price_expect` int(4) NOT NULL COMMENT '产品单价期望值',
  `unit_price_relax_value` int(4) NOT NULL COMMENT '产品购买单价可放松值',
  `unit_price_final` int(4) NULL DEFAULT NULL COMMENT '最终产品交易单价',
  `priority` int(4) NOT NULL COMMENT '优先级',
  PRIMARY KEY (`Id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of product_pur
-- ----------------------------
INSERT INTO `product_pur` VALUES ('B', 20, 5, 5, 0, 5);

-- ----------------------------
-- Table structure for product_sup
-- ----------------------------
DROP TABLE IF EXISTS `product_sup`;
CREATE TABLE `product_sup`  (
  `Id` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '产品生产商编号',
  `profit_expect` int(4) NOT NULL COMMENT '产品利润期望值',
  `profit_relax_value` int(4) NOT NULL COMMENT '产品利润可放松值',
  `profit_final` int(4) NULL DEFAULT NULL COMMENT '产品最终利润',
  `priority` int(4) NOT NULL COMMENT '优先级',
  PRIMARY KEY (`Id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of product_sup
-- ----------------------------
INSERT INTO `product_sup` VALUES ('A', 5, 5, 0, 5);

-- ----------------------------
-- Table structure for r_material_dis
-- ----------------------------
DROP TABLE IF EXISTS `r_material_dis`;
CREATE TABLE `r_material_dis`  (
  `trans_id` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '运送单号',
  `r_sup_id` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '原料提供商编号',
  `p_sup_id` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '产品生产商编号',
  PRIMARY KEY (`trans_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of r_material_dis
-- ----------------------------
INSERT INTO `r_material_dis` VALUES ('1', 'C', 'A');

-- ----------------------------
-- Table structure for r_material_sup
-- ----------------------------
DROP TABLE IF EXISTS `r_material_sup`;
CREATE TABLE `r_material_sup`  (
  `Id` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '原材料提供商编号',
  `total_cost_expect` int(4) NOT NULL COMMENT '原材料固定总费用期望值',
  `total_cost_relax_value` int(4) NOT NULL COMMENT '原材料固定总费用可放松值',
  `total_cost_priority` int(1) NOT NULL COMMENT '原材料固定总费用优先级',
  `unit_cost_expect` int(4) NOT NULL COMMENT '原材料变动单位费用期望值',
  `unit_cost_relax_value` int(4) NOT NULL COMMENT '原材料变动单位费用可放松值',
  `unit_cost_priority` int(1) NOT NULL COMMENT '原材料变动单位费用优先级',
  PRIMARY KEY (`Id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of r_material_sup
-- ----------------------------
INSERT INTO `r_material_sup` VALUES ('C', 5, 5, 5, 5, 5, 5);

-- ----------------------------
-- Table structure for r_material_trans
-- ----------------------------
DROP TABLE IF EXISTS `r_material_trans`;
CREATE TABLE `r_material_trans`  (
  `Id` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '原材料运输商编号',
  `r_material_num` int(4) NOT NULL COMMENT '原材料数目',
  `trans_profit_expect` int(4) NOT NULL COMMENT '运输费用期望值',
  `trans_profit_relax_value` int(4) NOT NULL COMMENT '运输费用可放松值',
  `priority` int(1) NOT NULL COMMENT '优先级',
  PRIMARY KEY (`Id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of r_material_trans
-- ----------------------------
INSERT INTO `r_material_trans` VALUES ('D', 20, 5, 5, 5);

SET FOREIGN_KEY_CHECKS = 1;
