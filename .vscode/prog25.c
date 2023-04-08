#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

#define MAX_LEVEL 10    // 最大关卡数

int level = 1;          // 当前关卡数
int player_x, player_y; // 玩家当前坐标
int box_x, box_y;       // 箱子当前坐标
int target_x, target_y; // 目标点坐标

int map[MAX_LEVEL][12][12] = {
    {   // 第 1 关地图
        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
        {1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1},
        {1, 2, 0, 0, 0, 0, 0, 0, 3, 2, 1},
        {1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1},
        {1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1},
        {1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1},
        {1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1},
        {1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1},
        {1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1},
        {1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1},
        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
    },
    {   // 第 2 关地图
        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
        {1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1},
        {1, 2, 0, 0, 0, 0, 0, 0, 2, 2, 1},
        {1, 2, 3, 0, 0, 0, 0, 0, 0, 2, 1},
        {1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1},
        {1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1},
        {1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1},
        {1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1},
        {1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1},
        {1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1},
        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
    }
    // 可以继续添加更多关卡的地图
};

void init_map() {
    int i, j;
    for (i = 0; i < 12; i++) {
        for (j = 0; j < 12; j++) {
            if (map[level - 1][i][j] == 2) {
                player_x = i;
                player_y = j;
            } else if (map[level - 1][i][j] == 3) {
                box_x = i;
                box_y = j;
            } else if (map[level - 1][i][j] == 4) {
                target_x = i;
                target_y = j;
            }
        }
    }
}

void display_map() {
    int i, j;
    system("cls");
    printf("PushBox (Level %d)\n", level);
    printf("WASD for movement, Q to quit\n");
    for (i = 0; i < 12; i++) {
        for (j = 0; j < 12; j++) {
            if (map[level - 1][i][j] == 1) {
                printf("# ");
            } else if (i == player_x && j == player_y) {
                printf("@ ");
            } else if (i == box_x && j == box_y) {
                printf("$ ");
            } else if (i == target_x && j == target_y) {
                printf(". ");
            } else {
                printf("  ");
            }
        }
        printf("\n");
    }
}

void move(int dx, int dy) {
    int new_player_x = player_x + dx;
    int new_player_y = player_y + dy;
    if (map[level - 1][new_player_x][new_player_y] != 1) {
        // 尝试推箱子
        if (new_player_x == box_x && new_player_y == box_y) {
            int new_box_x = box_x + dx;
            int new_box_y = box_y + dy;
            if (map[level - 1][new_box_x][new_box_y] != 1) {
                box_x = new_box_x;
                box_y = new_box_y;
            }
        }
        player_x = new_player_x;
        player_y = new_player_y;
    }
}

int check_win() {
    return box_x == target_x && box_y == target_y;
}

int main() {
    char c;
    init_map();
    while (c = getch()) {
        switch (c) {
        case 'w': move(-1, 0); break;
        case 'a': move(0, -1); break;
        case 's': move(1, 0); break;
        case 'd': move(0, 1); break;
        case 'q': exit(0);
        }
        if (check_win()) {
            level++;
            if (level > MAX_LEVEL) {
                printf("You win!\n");
                exit(0);
            } else {
                init_map();
            }
        }
        display_map();
    }
    return 0;
}