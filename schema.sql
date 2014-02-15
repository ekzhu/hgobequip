drop table if exists entries;
create table entries (
	id integer primary key autoincrement,
	equip_id string not null unique,
	group_name string not null,
	category string,
	case_id string,
	model string,
	manufacturer string,
	nick string,
	status string,
	borrower string,
	check_out_date string,
	note string,
	photo string,
	foreign key(group_name) references equip_group(group_name)
);
drop table if exists equip_group;
create table equip_group (
	group_name string primary key,
	photo string
);
insert into entries values (1, 'M-1', 'R200', '望远镜', '', 'R200主镜', '', '', '', '', '', '', '');
insert into entries values (2, 'S-1', 'R200', '望远镜', '', 'R200寻星镜架', '', '', '', '', '', '', '');
insert into entries values (3, 'S-2', 'R200', '望远镜', '', 'R200寻星镜', '', '', '', '', '', '', '');
insert into entries values (4, 'S-3', 'R200', '望远镜', '', 'R200目镜转接口', '', '', '', '', '', '', '');
insert into entries values (5, 'M-2', 'EQ6', '赤道仪', '', 'EQ6手控器1', '', '', '', '', '', '', '');
insert into entries values (6, 'M-3', 'EQ6', '赤道仪', '', 'EQ6主体', '', '', '', '', '', '', '');
insert into entries values (7, 'M-4', 'EQ6', '赤道仪', '', 'EQ6手控器2', '', '', '', '', '', '', '');
insert into entries values (8, 'L-1', 'EQ6', '赤道仪', '', 'EQ6手控器线1', '', '', '', '', '', '', '');
insert into entries values (9, 'L-2', 'EQ6', '赤道仪', '', 'EQ6手控器线2', '', '', '', '', '', '', '');
insert into entries values (10, 'M-5', 'EM11老', '赤道仪', '', 'EM11老主体', '', '', '', '', '', '', '');
insert into entries values (11, 'M-6', 'EM11老', '赤道仪', '', 'EM11老手控器', '', '', '', '', '', '', '');
insert into entries values (12, 'S-4', 'EM11老', '赤道仪', '', 'EM11老大螺丝', '', '', '', '', '', '', '');
insert into entries values (13, 'S-5', 'EM11老', '赤道仪', '', 'EM11老重锤杆', '', '', '', '', '', '', '');
insert into entries values (14, 'M-7', 'GP2N', '赤道仪', '', 'GP2N主体', '', '', '', '', '', '', '');
insert into entries values (15, 'S-6', 'GP2N', '赤道仪', '', 'GP2N电池盒', '', '', '', '', '', '', '');
insert into entries values (16, 'M-8', 'GP2N', '赤道仪', '', 'GP2N手控器', '', '', '', '', '', '', '');
insert into entries values (17, 'L-19', 'GP2N', '赤道仪', '', 'GP2N手控器线1', '', '', '', '', '', '', '');
insert into entries values (18, 'L-3', 'GP2N', '赤道仪', '', 'GP2N手控器线2', '', '', '', '', '', '', '');
insert into entries values (19, 'L-4', 'GP2N', '赤道仪', '', 'GP2N电机线', '', '', '', '', '', '', '');
insert into entries values (20, 'S-7', 'GP2N', '赤道仪', '', 'GP2N重锤杆', '', '', '', '', '', '', '');
insert into entries values (21, 'M-9', 'GP2老', '赤道仪', '', 'GP2老主体', '', '', '', '', '', '', '');
insert into entries values (22, 'S-8', 'GP2老', '赤道仪', '', 'GP2老重锤杆', '', '', '', '', '', '', '');
insert into entries values (23, 'S-9', 'GP2老', '赤道仪', '', 'GP2老电源', '', '', '', '', '', '"GP2N,GP2老通用电源"', '');
insert into entries values (24, 'S-10', 'GP2老', '赤道仪', '', 'GP2老光害滤镜', '', '', '', '', '', '', '');
insert into entries values (25, 'S-11', 'GP2老', '赤道仪', '', 'GP2老目镜', '', '', '', '', '', '', '');
insert into entries values (26, 'M-10', 'CG5', '赤道仪', '', 'CG5主体', '', '', '', '', '', '', '');
insert into entries values (27, 'S-12', 'CG5', '赤道仪', '', 'CG5重锤杆', '', '', '', '', '', '、。。', '');
insert into entries values (28, 'S-13', 'CG5', '赤道仪', '', 'CG5云台', '', '', '', '', '', '', '');
insert into entries values (29, 'M-11', 'CG5', '赤道仪', '', 'CG5手控器', '', '', '', '', '', '', '');
insert into entries values (30, 'L-5', 'CG5', '赤道仪', '', 'CG5 DEC线', '', '', '', '', '', '', '');
insert into entries values (31, 'L-6', 'CG5', '赤道仪', '', 'CG5 汽车电源', '', '', '', '', '', '', '');
insert into entries values (32, 'S-14', '景德80ED', '望远镜', '', '景德80ED云台板', '', '', '', '', '', '', '');
insert into entries values (33, 'M-12', '景德80ED', '望远镜', '', '景德80ED主体', '', '', '', '', '', '', '');
insert into entries values (34, 'S-15', '景德80ED', '望远镜', '', '景德80ED抱箍1', '', '', '', '', '', '', '');
insert into entries values (35, 'S-16', '景德80ED', '望远镜', '', '景德80ED抱箍2', '', '', '', '', '', '', '');
insert into entries values (36, 'S-17', '景德80ED', '望远镜', '', '景德80ED转接环1', '', '', '', '', '', '2'' EXTENDER', '');
insert into entries values (37, 'S-18', '景德80ED', '望远镜', '', '景德80ED转接环2', '', '', '', '', '', '', '');
insert into entries values (38, 'S-19', '景德80ED', '望远镜', '', '景德80ED转接环3', '', '', '', '', '', '编号C', '');
insert into entries values (39, 'S-20', '景德80ED', '望远镜', '', '景德80ED转接环4', '', '', '', '', '', '', '');
insert into entries values (40, 'S-21', '景德80ED', '望远镜', '', '景德80ED转接环5', '', '', '', '', '', '2''PHOTO ADAPTER', '');
insert into entries values (41, 'S-22', '景德80ED', '望远镜', '', '景德80ED延长管1', '', '', '', '', '', '', '');
insert into entries values (42, 'S-23', '景德80ED', '望远镜', '', '景德80ED延长管2', '', '', '', '', '', '', '');
insert into entries values (43, 'S-24', '景德80ED', '望远镜', '', '景德80ED延长管3', '', '', '', '', '', '', '');
insert into entries values (44, 'S-25', '景德80ED', '望远镜', '', '景德80ED延长管4', '', '', '', '', '', '', '');
insert into entries values (45, 'S-26', '景德80ED', '目镜', '', '景德80ED目镜1', '', '', '', '', '', 'PL25MM', '');
insert into entries values (46, 'S-27', '景德80ED', '目镜', '', '景德80ED十字镜', '', '', '', '', '', '', '');
insert into entries values (47, 'S-28', '景德80ED', '望远镜', '', '景德80ED转角镜1', '', '', '', '', '', 'CELESTRON 1 /4''', '');
insert into entries values (48, 'S-29', '景德80ED', '望远镜', '', '景德80ED转角镜2', '', '', '', '', '', 'meade', '');
insert into entries values (49, 'M-13', 'Celestron127mm', '望远镜', '', 'Celestron127mm主体', '', '', '', '', '', '', '');
insert into entries values (50, 'S-30', 'Celestron127mm', '望远镜', '', 'Celestron127mm转接环1', '', '', '', '', '', 'T-ADAPTER-SC', '');
insert into entries values (51, 'S-31', 'Celestron127mm', '望远镜', '', 'Celestron127mm寻星镜', '', '', '', '', '', '', '');
insert into entries values (52, 'S-32', 'Celestron127mm', '望远镜', '', 'Celestron127mm寻星镜架', '', '', '', '', '', '', '');
insert into entries values (53, 'S-33', 'Celestron127mm', '望远镜', '', 'Celestron127mm转角镜接环', '', '', '', '', '', '', '');
insert into entries values (54, 'S-34', 'Celestron127mm', '望远镜', '', 'Celestron127mm转角镜', '', '', '', '', '', '分辨率2''', '');
insert into entries values (55, 'M-14', 'QHY8CCD', 'CCD', '', 'QHY8CCD主体', '', '', '', '', '', '', '');
insert into entries values (56, 'L-7', 'QHY8CCD', 'CCD', '', 'QHY8CCD电源适配器', '', '', '', '', '', '', '');
insert into entries values (57, 'M-15', 'QHY6CCD', 'CCD', '', 'QHY6CCD主体', '', '', '', '', '', '', '');
insert into entries values (58, 'L-8', 'QHY6CCD', 'CCD', '', 'QHY6CCD连接线USB', '', '', '', '', '', '', '');
insert into entries values (59, 'L-9', 'QHY6CCD', 'CCD', '', 'QHY6CCD连接线', '', '', '', '', '', '', '');
insert into entries values (60, 'M-16', 'ApogeeU6', 'CCD', '', 'ApogeeU6主体', '', '', '', '', '', '', '');
insert into entries values (61, 'M-17', 'QHY5CCD', 'CCD', '', 'QHY5CCD主体', '', '', '', '', '', '', '');
insert into entries values (62, 'L-10', 'QHY5CCD', 'CCD', '', 'QHY5CCD连接线USB', '', '', '', '', '', '', '');
insert into entries values (63, 'L-11', 'QHY5CCD', 'CCD', '', 'QHY5CCD连接线', '', '', '', '', '', '', '');
insert into equip_group (group_name) values ('R200');
insert into equip_group (group_name) values ('QHY6CCD');
insert into equip_group (group_name) values ('QHY8CCD');
insert into equip_group (group_name) values ('Celestron127mm');
insert into equip_group (group_name) values ('ApogeeU6');
insert into equip_group (group_name) values ('QHY5CCD');
insert into equip_group (group_name) values ('EQ6');
insert into equip_group (group_name) values ('GP2老');
insert into equip_group (group_name) values ('EM11老');
insert into equip_group (group_name) values ('景德80ED');
insert into equip_group (group_name) values ('CG5');
insert into equip_group (group_name) values ('GP2N');
