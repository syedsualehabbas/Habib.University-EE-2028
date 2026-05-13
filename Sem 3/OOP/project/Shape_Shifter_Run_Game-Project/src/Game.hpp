#ifndef GAME_HPP
#define GAME_HPP

#include <SFML/Graphics.hpp>
#include <vector>
#include <memory>
#include "Player.hpp"
#include "Wall.hpp"
#include "Obstacle.hpp"
#include "HeartPickup.hpp"

class Game
{
public:
    enum class GameLevel { Level1, Level2, Level3 };
    Game();
    void run();
private:
    sf::RenderWindow window;
    sf::Font font;
    bool isRunning;
    sf::ConvexShape platform;
    Player player;
    std::vector<std::unique_ptr<Wall>> walls;
    std::vector<std::unique_ptr<Obstacle>> obstacles;
    std::vector<HeartPickup> heartPickups;
    std::vector<FallingHeart> fallingHearts;
    sf::Clock wallSpawnClock, obstacleSpawnClock, gameTimeClock;
    int score;
    GameLevel currentLevel;
    int lives = 3;
    const int maxLives = 3;
    int wallsSinceLastHeart = 0;
    int nextHeartSpawnWalls = 6;

    float getWallSpeed();
    float getWallSpawnInterval();
    bool storyScreen();
    bool levelSelectScreen();
    bool welcomeScreen();
    bool gameOverScreen();
    bool checkCollision(const Wall& wall);
    bool checkObstacleCollision();
    void updateGame(float dt);
    void drawGame();
    void gameLoop();
};

#endif // GAME_HPP