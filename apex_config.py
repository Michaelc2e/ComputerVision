# ==============================================================================
# M_APEX LEGENDS COMPUTER VISION ASSISTED ANTI-RECOIL(FREE VER.)
# Version: 3.12 (Jan 17, 2024)
# by Michael
# Any feedback, please email: M_ComputerVision@outlook.com
# or send private message via forum on ConsoleTuner.com

# ==============================================================================
# The credit goes, in the first place, to J2Kbr (Jefferson Koppe from 
# ConsoleTuner.com) who developed the original script of COMPUTER VISION 
# ASSISTED ANTI-RECOIL FOR APEX LEGENDS.
# This M_APEX CV script is developed based on the v1.49(Sep 8, 2021) of J2Kbr's 
# APEX CV script.

# ==============================================================================
# !ATTENTION! This GCV script was created, trained and tested using the game 
# settings listed below. Different aming settings may cause this script to 
# not work as intended.
# - Response Curve: CLASSIC
# - Look Deadzone:  SMALL

# ==============================================================================
#               Language
# ==============================================================================
# Set LANGUAGE_DETECT according to the language used in the game:
# 根据游戏语言进行设置:
LANGUAGE_DETECT = 1
#     1: [EN] English
#     2: [ES] Español
#     3: [DE] Deutsch    
#     4: [FR] Français
#     5: [PT] Portugais
#     6: [RU] Русский
#     7: [CN] 简体中文
#     8: [TC] 繁體中文
#     9: [JP] 日本語
#    10: [KR] 한국어

# ==============================================================================
#               Resolution
# ==============================================================================
# Set RESOLUTION_TYPE:
# 根据显示分辨率进行设置:
RESOLUTION_TYPE = 0
# 0: Default(1920*1080p, 2560*1440p or 3840*2160p),
# 1: 1728*1080,

# ==============================================================================
#               Performance Mode
# ==============================================================================
# Performance Mode: to increase performance of anti-recoil process.
# If performance mode is on, captured frame display will be unavailable.
# 性能模式: 提升反后坐力表现。
# 如果开启性能模式，采集画面将不可预览。
PERFORMANCE_MODE = 0
# 0: off        1: on  

# ==============================================================================
#               Adjust the brightness level of the templates
# ==============================================================================
# This feature will help when the brightness in the game setting is changed or
# the brightness of displayed image is different from the templates.
# Two demo templates will be shown, the original and the adjusted. 
# Press any key to continue.
DEMO_TEMPLATE_BRIGHTNESS_PREVIEW = 0
# 0: off        1: on
delta = 1.00
# If delta < 1.00, it will darken the templates.  
# If delta > 1.00, it will brighten the templates.
# By default, delta = 1.00  

# ==============================================================================
#               Alternative Detection Method 
# ==============================================================================
# This feature offers an alternative detection method. 
# Try using this feature, only when the weapon tags, fire modes or optics are 
# detected incorrectly.
ALTERNATE_DETECT_WEAPON = 0
# 0: off        1: on  
ALTERNATE_DETECT_FIREMODE = 0
# 0: off        1: on  
ALTERNATE_DETECT_OPTICS = 0
# 0: off        1: on

# ==============================================================================
#               Detect Optics with Variable Zoom
# ==============================================================================
DETECT_VARIABLE_ZOOM = 0
# 0: off(
# 		Manual zoom toggle method for VARIABLE AOG       (or VARIABLE HOLO): 
#           L2/LT + L3/LS     = toggle between 2X and 4X (or 1X and 2X)
#           L2/LT + Circle/B  = 4X                       (or 2X)
#           L2/LT + Cross/A   = 2X                       (or 1X)
# 	 	)
# 
# 1: on(
# 		cv-detect for optics of 1X-2X VARIABLE HOLO and 2X-4X VARIABLE AOG.
# 		Known flaws: 
# 		1) when the background is bright, the 4x zoom will not be detected.
# 		2) Not reliable. It will fail sometimes.
# 		Experimental feature! 
#		)

# ==============================================================================
#               Data Set
# ==============================================================================
# Set DATA_SET = 1 to compute the anti-recoil values for regular controllers 
# or XIM. If using mouse and the official keyboard and mouse Input Translator 
# for Apex Legends, configure DATA_SET = 2 to compute the anti-recoil values 
# for mouse raw input.
DATA_SET = 1
# When using DATA_SET = 1 it may be necessary also adjust the DEADZONE_SIZE 
# according the game settings, specially when using in conjunction with XIM.
# The default value for PlayStation 4 is 9.80 and for Xbox One is 10.60.
DEADZONE_SIZE = 9.80

# ==============================================================================
#               Platform
# ==============================================================================
# Set NINTENDO_SWITCH = 1 when using this GCV Script on Nintendo Switch.
NINTENDO_SWITCH = 0

# ==============================================================================
#               Rapid Fire
# ==============================================================================
# Turn off rapid fire for specific weapons: /关闭特定武器的快速射击： 
# 0: off/关闭,   1: on/开启 
RF_P2020            = 1     # P2020         / P2020手 
RF_R301_SINGLE      = 1     # R-301         / R-301卡宾 
RF_G7SCOUT_SINGLE   = 1     # G7 SCOUT      / G7侦查 
RF_G7SCOUT_BURST    = 1      
RF_3030             = 1     # 30-30         / 30-30
RF_PROWLER_SINGLE   = 1     # PROWLER       / 猎兽冲锋 
RF_PROWLER_BURST    = 1      
RF_HEMLOK_SINGLE    = 1     # HEMLOK        / 赫姆洛克突击步 
RF_HEMLOK_BURST     = 1
RF_FLATLINE_SINGLE  = 1     # FLATLINE      / 平行步 
RF_PEACEKEEPER      = 1     # PEACEKEEPER   / 和平捍卫者散弹 
RF_MASTIFF          = 1     # MASTIFF       / 敖犬散弹 
RF_SENTINEL         = 1     # SENTINEL      / 哨兵狙击步 
RF_WINGMAN          = 1     # WINGMAN       / 辅助手 
RF_CHARGE_RIFLE     = 1     # CHARGE RIFLE  / 充能步 
RF_LONGBOW          = 1     # LONGBOW       / 长弓
RF_KRABER           = 1     # KRABER        / 克雷贝尔狙击 

# ==============================================================================
#               Anti-recoil
# ==============================================================================
# The anti-recoil computed values directly depends on the gaming system and 
# game sensitivity configuration. !IMPORTANT! Go to FIRING RANGE and adjust 
# the horizontal and vertical global scaling below for the best results to 
# your gaming system and in-game sensitivity.
# 设置反后坐力全局参数(H:水平方向, V:垂直方向):
GLOBAL_HSCALE = 2.90
GLOBAL_VSCALE = 3.19

# The strength of anti-recoil will be affected by different optical sights equipped.
# Optics scaling adjustments for each magnification:
# 设置不同倍镜的调整系数
# H: Horizontal     V: Vertical
# H: 水平方向        V: 垂直方向
# ======================= 1x ===================================================
OPTICS_1x_H = 0.55
OPTICS_1x_V = 0.55
# ======================= 2x ===================================================
OPTICS_2x_H = 0.77
OPTICS_2x_V = 0.77
# ======================= 3x ===================================================
OPTICS_3x_H = 1.00
OPTICS_3x_V = 1.00
# ======================= 4x ===================================================
OPTICS_4x_H = 1.21
OPTICS_4x_V = 1.21

# In Apex Legends, the recoil strength of weapons will be affected by whether the target
# is hit or not, and the recoil strength is slightly stronger when the target is hit. 
# Hence, it's necessary to adjust the anti-recoil strength for the target hit or unhit.
# In GAMEPLAY setting section, set Crosshair Damage Feedback to "X" or "X w/Shield Icon"
# 在Apex英雄游戏里，射击是否击中目标会影响武器后坐力，而且后坐力强度在击中目标时会稍微大一些。
# 因此，根据是否击中目标调整压 力度是有必要的。
# 游戏设置，设置准星伤害反馈为“准心X”或“带有盾标的准星X”

# Anti-recoil strength adjustment for target hit:
# 击中目标时，压 强度调整：
TargetHit_H = 1.00
TargetHit_V = 1.16
# Anti-recoil strength adjustment for target unhit:
# 没有击中目标时，压 强度调整：
TargetUnhit_H = 1.00
TargetUnhit_V = 1.00


# Fine-tune anti-recoil values of specific weapons(part-I):
# 精调特定武器的反后坐力系数（第一部分）：
# H: Horizontal(水平方向)   V: Vertical(垂直方向)
# ADS: 机瞄             HIP: 腰射
# ======================= RE-45自动手 ==========================================
RE45_H_ADS			= 1.00
RE45_V_ADS			= 1.00
RE45_H_HIP			= 1.00
RE45_V_HIP			= 1.00
# ======================= P2020手  =============================================
P2020_H_ADS			= 1.00
P2020_V_ADS			= 1.00
P2020_H_HIP			= 1.00
P2020_V_HIP			= 1.00
# ======================= R-301卡宾  ===========================================
R301_H_ADS			= 1.00
R301_V_ADS			= 1.00
R301_H_HIP			= 1.00
R301_V_HIP			= 1.00
R301_H_Auto			= 1.00
R301_V_Auto			= 1.00
R301_H_Single		= 1.00
R301_V_Single		= 1.00
# ======================= R-99冲锋  ============================================
R99_H_ADS			= 0.95
R99_V_ADS			= 1.05
R99_H_HIP			= 1.00
R99_V_HIP			= 1.00
# ======================= CAR-L / CAR轻型  ===================================
CARL_H_ADS			= 1.00
CARL_V_ADS			= 1.00
CARL_H_HIP			= 1.00
CARL_V_HIP			= 1.00
# ======================= CAR-H / CAR重型  ===================================
CARH_H_ADS			= 1.00
CARH_V_ADS			= 1.00
CARH_H_HIP			= 1.00
CARH_V_HIP			= 1.00
# ======================= Alternator / 转换者冲锋  ==============================
Alternator_H_ADS	= 1.00
Alternator_V_ADS	= 0.88
Alternator_H_HIP	= 1.00
Alternator_V_HIP	= 1.00
# ======================= G7 Scout / G7侦查  ===================================
G7Scout_H_ADS		= 1.00
G7Scout_V_ADS		= 1.00
G7Scout_H_HIP		= 1.00
G7Scout_V_HIP		= 1.00
G7Scout_H_Burst		= 1.00
G7Scout_V_Burst		= 1.00
G7Scout_H_Single	= 1.00
G7Scout_V_Single	= 1.00
# ======================= Rampage / 暴走 =======================================
Rampage_H_ADS		= 1.00
Rampage_V_ADS		= 1.00
Rampage_H_HIP		= 1.00
Rampage_V_HIP		= 1.00
Rampage_H_Turbo		= 1.00
Rampage_V_Turbo		= 1.00
# ======================= 30-30 Repeater / 30-30连发  ==========================
Repeater3030_H_ADS	= 1.00
Repeater3030_V_ADS	= 1.00
Repeater3030_H_HIP	= 1.00
Repeater3030_V_HIP	= 1.00
# ======================= Wingman / 辅助手  ====================================
Wingman_H_ADS		= 1.00
Wingman_V_ADS		= 1.00
Wingman_H_HIP		= 1.00
Wingman_V_HIP		= 1.00
# ======================= Spitfire / 喷火轻机 ===================================
Spitfire_H_ADS		= 1.00
Spitfire_V_ADS		= 1.00
Spitfire_H_HIP		= 1.00
Spitfire_V_HIP		= 1.00
# ======================= Prowler / 猎兽冲锋  ===================================
Prowler_H_ADS		= 0.85
Prowler_V_ADS		= 0.85
Prowler_H_HIP		= 1.00
Prowler_V_HIP		= 1.00
Prowler_H_Auto		= 1.00
Prowler_V_Auto		= 1.00
Prowler_H_Burst		= 1.00
Prowler_V_Burst		= 1.00
Prowler_H_Single	= 1.00
Prowler_V_Single	= 1.00
# ======================= Hemlok / 赫姆洛克突击步  ===============================
Hemlok_H_ADS		= 1.00
Hemlok_V_ADS		= 1.00
Hemlok_H_HIP		= 1.00
Hemlok_V_HIP		= 1.00
Hemlok_H_Burst		= 0.90
Hemlok_V_Burst		= 0.90
Hemlok_H_Single		= 1.00
Hemlok_V_Single		= 1.00
# ======================= Flatline / 平行步  ===================================
Flatline_H_ADS		= 1.00
Flatline_V_ADS		= 1.00
Flatline_H_HIP		= 1.00
Flatline_V_HIP		= 1.00
Flatline_H_Auto		= 1.00
Flatline_V_Auto		= 1.00
Flatline_H_Single	= 1.00
Flatline_V_Single	= 1.00
# ======================= Volt / 电能冲锋  ======================================
Volt_H_ADS			= 1.00
Volt_V_ADS			= 1.00
Volt_H_HIP			= 1.00
Volt_V_HIP			= 1.00
# ======================= Devotion / 专注轻机  ==================================
Devotion_H_ADS		= 1.00
Devotion_V_ADS		= 1.00
Devotion_H_HIP		= 1.00
Devotion_V_HIP		= 1.00
Devotion_H_Turbo	= 1.00
Devotion_V_Turbo	= 1.00
# ======================= Havoc / 哈沃克步  =====================================
Havoc_H_ADS			= 0.89
Havoc_V_ADS			= 0.89
Havoc_H_HIP			= 1.00
Havoc_V_HIP			= 1.00
Havoc_H_Turbo		= 1.00
Havoc_V_Turbo		= 1.00
# ======================= L-Star / L-STAR能量机  ===============================
LStar_H_ADS			= 1.00
LStar_V_ADS			= 1.00
LStar_H_HIP			= 1.00
LStar_V_HIP			= 1.00
# ======================= Mini移动重机  =========================================
MMinigun_H_ADS		= 1.00
MMinigun_V_ADS		= 1.00
MMinigun_H_HIP		= 1.00
MMinigun_V_HIP		= 1.00
# ======================= Mini重机  ============================================
Minigun_H_ADS		= 1.00
Minigun_V_ADS		= 1.00
Minigun_H_HIP		= 1.00
Minigun_V_HIP		= 1.00
# ======================= Nemesis / 复仇女神 ===============================
Nemesis_H_ADS		= 1.00
Nemesis_V_ADS		= 1.00
Nemesis_H_HIP		= 1.00
Nemesis_V_HIP		= 1.00


# Fine-tune anti-recoil values of specific weapons(part-II):
# 精调特定武器的反后坐力系数（第二部分）：
# H: Horizontal(水平方向)   V: Vertical(垂直方向)
# 1X:1倍镜   2X:2倍镜   3X:3倍镜   4X:4倍镜
# ======================= RE-45自动手 ==========================================
RE45_H_1X		= 1.00
RE45_V_1X		= 1.00
RE45_H_2X		= 1.00
RE45_V_2X		= 1.00
# ======================= P2020手  =============================================
P2020_H_1X		= 1.00
P2020_V_1X		= 1.00
P2020_H_2X		= 1.00
P2020_V_2X		= 1.00
# ======================= R-301卡宾  ===========================================
R301_H_1X		= 1.00
R301_V_1X		= 1.00
R301_H_2X		= 1.00
R301_V_2X		= 1.00
R301_H_3X		= 1.00
R301_V_3X		= 1.00
R301_H_4X		= 1.00
R301_V_4X		= 1.00
# ======================= Spitfire / 喷火轻机 ===================================
Spitfire_H_1X	= 1.00
Spitfire_V_1X   = 1.00
Spitfire_H_2X   = 1.00
Spitfire_V_2X   = 1.00
Spitfire_H_3X   = 1.00
Spitfire_V_3X   = 1.00
Spitfire_H_4X   = 1.00
Spitfire_V_4X   = 1.00
# ======================= R-99冲锋  ============================================
R99_H_1X		= 1.00
R99_V_1X		= 1.00
R99_H_2X		= 1.00
R99_V_2X		= 1.00
# ======================= Alternator / 转换者冲锋  ==============================
Alternator_H_1X	= 1.00
Alternator_V_1X	= 1.00
Alternator_H_2X	= 1.00
Alternator_V_2X	= 1.00
# ======================= G7 Scout / G7侦查  ===================================
G7_H_1X		    = 1.00
G7_V_1X		    = 1.00
G7_H_2X		    = 1.00
G7_V_2X		    = 1.00
G7_H_3X		    = 1.00
G7_V_3X		    = 1.00
G7_H_4X		    = 1.00
G7_V_4X		    = 1.00
# ======================= CAR-L / CAR轻型  ===================================
CARL_H_1X		= 1.00
CARL_V_1X		= 1.00
CARL_H_2X		= 1.00
CARL_V_2X		= 1.00
# ======================= CAR-H / CAR重型  ===================================
CARH_H_1X		= 1.00
CARH_V_1X		= 1.00
CARH_H_2X		= 1.00
CARH_V_2X		= 1.00
# ======================= Rampage / 暴走 =======================================
Rampage_H_1X	= 1.00
Rampage_V_1X    = 1.00
Rampage_H_2X    = 1.00
Rampage_V_2X    = 1.00
Rampage_H_3X    = 1.00
Rampage_V_3X    = 1.00
Rampage_H_4X    = 1.00
Rampage_V_4X    = 1.00
# ======================= Prowler / 猎兽冲锋  ===================================
Prowler_H_1X	= 1.00
Prowler_V_1X	= 1.00
Prowler_H_2X	= 1.00
Prowler_V_2X	= 1.00
# ======================= Hemlok / 赫姆洛克突击步  ===============================
Hemlok_H_1X	    = 1.00
Hemlok_V_1X     = 1.00
Hemlok_H_2X     = 1.00
Hemlok_V_2X     = 1.00
Hemlok_H_3X     = 1.00
Hemlok_V_3X     = 1.00
Hemlok_H_4X     = 1.00
Hemlok_V_4X     = 1.00
# ======================= Flatline / 平行步  ===================================
Flatline_H_1X	= 1.00
Flatline_V_1X   = 1.00
Flatline_H_2X   = 1.00
Flatline_V_2X   = 1.00
Flatline_H_3X   = 1.00
Flatline_V_3X   = 1.00
Flatline_H_4X   = 1.00
Flatline_V_4X   = 1.00
# ======================= Volt / 电能冲锋  ======================================
Volt_H_1X   	= 1.00
Volt_V_1X	    = 1.00
Volt_H_2X	    = 1.00
Volt_V_2X   	= 1.00
# ======================= Devotion / 专注轻机  ==================================
Devotion_H_1X   = 1.00
Devotion_V_1X	= 1.00
Devotion_H_2X	= 1.00
Devotion_V_2X   = 1.00
Devotion_H_3X   = 1.00
Devotion_V_3X   = 0.90
Devotion_H_4X   = 1.00
Devotion_V_4X   = 1.00
# ======================= Havoc / 哈沃克步  =====================================
Havoc_H_1X  	= 1.00
Havoc_V_1X      = 1.00
Havoc_H_2X      = 1.00
Havoc_V_2X      = 1.00
Havoc_H_3X      = 0.90
Havoc_V_3X      = 0.90
Havoc_H_4X      = 1.00
Havoc_V_4X      = 1.00
# ======================= L-Star / L-STAR能量机  ===============================
LStar_H_1X	    = 1.00
LStar_V_1X      = 1.00
LStar_H_2X      = 1.00
LStar_V_2X      = 1.00
LStar_H_3X      = 1.00
LStar_V_3X      = 1.00
LStar_H_4X      = 1.00
LStar_V_4X      = 1.00
# ======================= Nemesis / 复仇女神 ===============================
Nemesis_H_1X	  = 1.00
Nemesis_V_1X      = 1.00
Nemesis_H_2X      = 1.00
Nemesis_V_2X      = 1.00
Nemesis_H_3X      = 1.00
Nemesis_V_3X      = 1.00
Nemesis_H_4X      = 1.00
Nemesis_V_4X      = 1.00


# Fine-tune anti-recoil values of specific weapons(part-III):
# 精调特定武器的反后坐力系数（第三部分）：
# This part is for anti-recoil timing adjust. +/- certain values.
# 这部分用于与压 时间相关的调整。增加或减少特定数值
# ======================= RE-45自动手 ==========================================
RE45_a  		    = 0.00
# ======================= P2020手  =============================================
P2020_a     		= 0.00
# ======================= R-301卡宾  ===========================================
R301_auto_a      	= 0.00
R301_single_a      	= 0.00
# ======================= Spitfire / 喷火轻机 ===================================
Spitfire_a      	= 0.00
# ======================= R-99冲锋  ============================================
R99_a       		= 0.00
# ======================= Alternator / 转换者冲锋  ==============================
Alternator_a    	= 0.00
# ======================= G7 Scout / G7侦查  ===================================
G7_burst_a       	= 0.00
G7_single_a       	= 0.00
# ======================= CAR-L / CAR轻型  ===================================
CARL_a      		= 0.00
# ======================= CAR-H / CAR重型  ===================================
CARH_a      		= 0.00
# ======================= Rampage / 暴走 =======================================
Rampage_a       	= 0.00
Rampage_turbo_a     = 0.00
# ======================= Prowler / 猎兽冲锋  ===================================
Prowler_auto_a     = 0.00
Prowler_burst_a     = 0.00
Prowler_single_a    = 0.00
# ======================= Hemlok / 赫姆洛克突击步  ===============================
Hemlok_burst_a      = 0.00
Hemlok_single_a     = 0.00
# ======================= Flatline / 平行步  ===================================
Flatline_auto_a     = 0.00
Flatline_single_a   = 0.00
# ======================= Volt / 电能冲锋  ======================================
Volt_a             	= 0.00
# ======================= Devotion / 专注轻机  ==================================
Devotion_a          = 0.00
Devotion_turbo_a    = 0.00
# ======================= Havoc / 哈沃克步  =====================================
Havoc_a             = 0.00
Havoc_turbo_a       = 0.00
# ======================= L-Star / L-STAR能量机  ===============================
LStar_a             = 0.00
# ======================= Nemesis / 复仇女神 ===============================
Nemesis_a           = 0.00

# Turn on/off the zoom track for mix-optic (1x/2x or 2x/4x optical sight)
# 1 = Turn on; 0 = Turn off
ZTRACK = 1

# ============= Customized Anti-recoil Data Set ============= 
# Set the USE_CUSTOMIZED_ANTIRECOIL_DATA = 1, then the ANTIRECOIL_CUSTOMIZED data 
# set will be used.
USE_CUSTOMIZED_ANTIRECOIL_DATA = 0
# 0: off        1: on

ANTIRECOIL_CUSTOMIZED = [

]

# ==============================================================================
# FROM THIS POINT NO CHANGE OR USER'S CUSTOMIZATION IS NEEDED
# ==============================================================================
from m_apexcv312a import *