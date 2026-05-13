#include "Game.hpp"
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <optional>
#include <cmath>
#include <string>
#include <cstdint>

Game::Game()
    : window(sf::VideoMode({800, 600}), "Shape Shifter Run"),
      isRunning(true),
      score(0),
      currentLevel(GameLevel::Level1)
{
    window.setFramerateLimit(60);
    srand(static_cast<unsigned>(time(0)));
    if (!font.openFromFile("arial.ttf"))
        if (!font.openFromFile("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
            font.openFromFile("C:\\Windows\\Fonts\\arial.ttf");

    platform.setPointCount(4);
    platform.setPoint(0, {50.f, 550.f});
    platform.setPoint(1, {750.f, 550.f});
    platform.setPoint(2, {750.f, 600.f});
    platform.setPoint(3, {50.f, 600.f});
    platform.setFillColor(sf::Color(80, 120, 200));
}

void Game::run()
{
    if (storyScreen())
        if (levelSelectScreen())
            if (welcomeScreen())
                gameLoop();
}

float Game::getWallSpeed()
{
    switch (currentLevel)
    {
        case GameLevel::Level1: return 120.f;
        case GameLevel::Level2: return 180.f;
        case GameLevel::Level3:
            return std::min(200.f + gameTimeClock.getElapsedTime().asSeconds() * 5.f, 350.f);
    }
    return 120.f;
}

float Game::getWallSpawnInterval()
{
    switch (currentLevel)
    {
        case GameLevel::Level1: return 2.5f;
        case GameLevel::Level2: return 2.0f;
        case GameLevel::Level3: return 1.8f;
    }
    return 2.5f;
}

bool Game::storyScreen()
{
    struct Star
    {
        sf::Vector2f pos;
        float radius;
        float phase;
        std::uint8_t baseAlpha;
    };

    std::vector<Star> stars;
    stars.reserve(140);
    for (int i = 0; i < 140; ++i)
    {
        Star s;
        s.pos = { static_cast<float>(rand() % 800), static_cast<float>(rand() % 600) };
        s.radius = 0.8f + static_cast<float>(rand() % 8) / 10.f;
        s.phase = static_cast<float>(rand() % 628) / 100.f;
        s.baseAlpha = static_cast<std::uint8_t>(180 + rand() % 60);
        stars.push_back(s);
    }

    sf::Clock starClock;

    struct Page { const char* text; unsigned int size; };
    std::vector<Page> pages = {
        {
            "In a world built from pure geometry, every shape has a purpose.\n"
            "Deep inside the Dimension Corridor, an ancient pathway of shifting walls\n"
            "and glowing gateways, lies the Core of Harmony the source that keeps\n"
            "the geometric universe balanced.",
            22u
        },
        { "But the Core is falling.", 28u },
        {
            "To restore stability, the Shape Guardians create a single hero: Shift,\n"
            "a small being with the rare ability to morph into any basic shape\n"
            "Triangle, Circle, or Square.",
            22u
        },
        { "Shift's mission is simple but dangerous:", 24u },
        {
            "The Corridor is filled with walls that have shape-shaped openings—\n"
            "circle pores, triangle slots, and square gaps. These walls move fast,\n"
            "and the path never slows down. To survive, Shift must instantly transform\n"
            "into the correct shape, perfectly matching each opening while running\n"
            "toward the Core.",
            22u
        },
        {
            "As Shift moves deeper, the walls become faster, the patterns more\n"
            "complex, and the fragments of corrupted geometry try to break the\n"
            "path apart. Only by mastering all three forms can Shift reach the\n"
            "Core and restore balance to the world.",
            22u
        },
        {
            "Every decision is instant.\n\n"
            "Every wall is a test.\n"
            "Every shape matters.\n\n"
            "Become the shape.\n"
            "Match the portal.\n"
            "Save the dimension.",
            26u
        }
    };

    std::size_t pageIndex = 0;
    sf::Clock blink;
    bool showHint = true;

    while (window.isOpen())
    {
        while (const std::optional<sf::Event> event = window.pollEvent())
        {
            if (event->is<sf::Event::Closed>()) { window.close(); return false; }
            if (auto* key = event->getIf<sf::Event::KeyPressed>())
            {
                if (key->code == sf::Keyboard::Key::Escape) { window.close(); return false; }
                if (key->code == sf::Keyboard::Key::Enter || key->code == sf::Keyboard::Key::Space)
                {
                    if (pageIndex + 1 < pages.size()) ++pageIndex;
                    else return true;
                }
            }
        }

        if (blink.getElapsedTime().asSeconds() > 0.5f)
        {
            showHint = !showHint;
            blink.restart();
        }

        float t = starClock.getElapsedTime().asSeconds();

        window.clear(sf::Color(2, 4, 10));
        sf::RectangleShape topGrad({800.f, 320.f});
        topGrad.setPosition({0.f, 0.f});
        topGrad.setFillColor(sf::Color(10, 15, 45));
        window.draw(topGrad);

        sf::RectangleShape bottomGrad({800.f, 280.f});
        bottomGrad.setPosition({0.f, 320.f});
        bottomGrad.setFillColor(sf::Color(3, 3, 18));
        window.draw(bottomGrad);

        sf::CircleShape nebula(260.f);
        nebula.setOrigin({260.f, 260.f});
        nebula.setPosition({250.f, 180.f});
        nebula.setFillColor(sf::Color(80, 40, 120, 90));
        window.draw(nebula);
        nebula.setRadius(230.f);
        nebula.setOrigin({230.f, 230.f});
        nebula.setPosition({580.f, 280.f});
        nebula.setFillColor(sf::Color(40, 120, 160, 75));
        window.draw(nebula);

        for (const auto& s : stars)
        {
            float twinkle = 0.5f + 0.5f * std::sin(t * 1.8f + s.phase);
            std::uint8_t alpha = static_cast<std::uint8_t>(twinkle * s.baseAlpha);
            sf::CircleShape starShape(s.radius);
            starShape.setOrigin({s.radius, s.radius});
            starShape.setPosition(s.pos);
            starShape.setFillColor(sf::Color(240, 240, 255, alpha));
            window.draw(starShape);
        }

        sf::CircleShape voidPortal(260.f);
        voidPortal.setOrigin({260.f, 260.f});
        voidPortal.setPosition({400.f, 260.f});
        voidPortal.setFillColor(sf::Color(5, 5, 10, 235));
        window.draw(voidPortal);

        sf::CircleShape glowRing(280.f);
        glowRing.setOrigin({280.f, 280.f});
        glowRing.setPosition({400.f, 260.f});
        glowRing.setFillColor(sf::Color(0, 0, 0, 0));
        glowRing.setOutlineThickness(4.f);
        glowRing.setOutlineColor(sf::Color(130, 210, 255, 120));
        window.draw(glowRing);

        sf::Text story(font, pages[pageIndex].text);
        story.setCharacterSize(pages[pageIndex].size);
        story.setFillColor(sf::Color(225, 235, 255));
        story.setOutlineThickness(3.f);
        story.setOutlineColor(sf::Color(15, 25, 65));
        sf::FloatRect sb = story.getLocalBounds();
        story.setOrigin({sb.position.x + sb.size.x / 2.f, sb.position.y + sb.size.y / 2.f});
        story.setPosition({400.f, 260.f});
        window.draw(story);

        if (showHint)
        {
            const char* hintText = pageIndex + 1 == pages.size()
                ? "Press Enter or Space to begin"
                : "Press Enter or Space to continue";
            sf::Text hint(font, hintText);
            hint.setCharacterSize(20);
            hint.setFillColor(sf::Color(190, 220, 255));
            sf::FloatRect hb = hint.getLocalBounds();
            hint.setOrigin({hb.position.x + hb.size.x / 2.f, hb.position.y + hb.size.y / 2.f});
            hint.setPosition({400.f, 520.f});
            window.draw(hint);
        }

        window.display();
    }
    return false;
}

bool Game::levelSelectScreen()
{
    sf::Text title(font, "Select Level");
    title.setCharacterSize(64);
    title.setFillColor(sf::Color(255, 200, 100));
    title.setOutlineThickness(3.f);
    title.setOutlineColor(sf::Color(10, 10, 30));
    sf::FloatRect tb = title.getLocalBounds();
    title.setOrigin({tb.position.x + tb.size.x / 2.f, tb.position.y + tb.size.y / 2.f});
    title.setPosition({400.f, 80.f});

    sf::Text lvls[3] = {
        sf::Text(font, "1 - Easy (Slow Walls)"),
        sf::Text(font, "2 - Medium (Faster Walls)"),
        sf::Text(font, "3 - Hard (Walls + Obstacles!)")
    };
    sf::Color colors[3] = {sf::Color(100, 255, 100), sf::Color(255, 200, 100), sf::Color(255, 100, 100)};
    float yPos[3] = {200.f, 280.f, 360.f};
    
    for (int i = 0; i < 3; i++)
    {
        lvls[i].setCharacterSize(32);
        lvls[i].setFillColor(colors[i]);
        lvls[i].setOutlineThickness(2.f);
        lvls[i].setOutlineColor(sf::Color(10, 10, 30));
        sf::FloatRect b = lvls[i].getLocalBounds();
        lvls[i].setOrigin({b.position.x + b.size.x / 2.f, b.position.y + b.size.y / 2.f});
        lvls[i].setPosition({400.f, yPos[i]});
    }

    sf::Text instruction(font, "Press ESC to quit");
    instruction.setCharacterSize(20);
    instruction.setFillColor(sf::Color(150, 150, 150));
    instruction.setOutlineThickness(1.5f);
    instruction.setOutlineColor(sf::Color(10, 10, 30));
    sf::FloatRect ib = instruction.getLocalBounds();
    instruction.setOrigin({ib.position.x + ib.size.x / 2.f, ib.position.y + ib.size.y / 2.f});
    instruction.setPosition({400.f, 500.f});

    while (window.isOpen())
    {
        while (const std::optional<sf::Event> event = window.pollEvent())
        {
            if (event->is<sf::Event::Closed>()) { window.close(); return false; }
            if (auto* key = event->getIf<sf::Event::KeyPressed>())
            {
                if (key->code == sf::Keyboard::Key::Num1) { currentLevel = GameLevel::Level1; return true; }
                if (key->code == sf::Keyboard::Key::Num2) { currentLevel = GameLevel::Level2; return true; }
                if (key->code == sf::Keyboard::Key::Num3) { currentLevel = GameLevel::Level3; return true; }
                if (key->code == sf::Keyboard::Key::Escape) { window.close(); return false; }
            }
        }
        window.clear(sf::Color(10, 15, 35));
        window.draw(title);
        for (int i = 0; i < 3; i++) window.draw(lvls[i]);
        window.draw(instruction);
        window.display();
    }
    return false;
}

bool Game::welcomeScreen()
{
    sf::Text title(font, "Shape Shifter Run");
    title.setCharacterSize(64);
    title.setFillColor(sf::Color(255, 200, 100));
    title.setOutlineThickness(3.f);
    title.setOutlineColor(sf::Color(10, 10, 30));
    sf::FloatRect tb = title.getLocalBounds();
    title.setOrigin({tb.position.x + tb.size.x / 2.f, tb.position.y + tb.size.y / 2.f});
    title.setPosition({400.f, 100.f});

    std::string levelText = "Level: " + std::string(currentLevel == GameLevel::Level1 ? "Easy" : 
        currentLevel == GameLevel::Level2 ? "Medium" : "Hard");
    sf::Text levelInfo(font, levelText);
    levelInfo.setCharacterSize(28);
    levelInfo.setFillColor(sf::Color(255, 150, 255));
    levelInfo.setOutlineThickness(2.f);
    levelInfo.setOutlineColor(sf::Color(10, 10, 30));
    sf::FloatRect lib = levelInfo.getLocalBounds();
    levelInfo.setOrigin({lib.position.x + lib.size.x / 2.f, lib.position.y + lib.size.y / 2.f});
    levelInfo.setPosition({400.f, 180.f});

    sf::Text instruction(font, "Press Enter to start");
    instruction.setCharacterSize(28);
    instruction.setFillColor(sf::Color(100, 255, 200));
    instruction.setOutlineThickness(2.f);
    instruction.setOutlineColor(sf::Color(10, 10, 30));
    sf::FloatRect ib = instruction.getLocalBounds();
    instruction.setOrigin({ib.position.x + ib.size.x / 2.f, ib.position.y + ib.size.y / 2.f});
    instruction.setPosition({400.f, 250.f});

    sf::Text controls[4] = {
        sf::Text(font, "Arrow Keys or A/D - Move Left and Right"),
        sf::Text(font, "Press 1 for Circle, 2 for Rectangle, 3 for Triangle"),
        sf::Text(font, "Match your shape with the hole to pass!"),
        sf::Text(font, currentLevel == GameLevel::Level3 ? "AVOID RED OBSTACLES!" : "")
    };
    sf::Color cColors[4] = {sf::Color(100, 200, 255), sf::Color(100, 200, 255), 
        sf::Color(255, 100, 150), sf::Color(255, 50, 50)};
    float cYPos[4] = {350.f, 400.f, 450.f, 500.f};
    
    for (int i = 0; i < 4; i++)
    {
        controls[i].setCharacterSize(18);
        controls[i].setFillColor(cColors[i]);
        controls[i].setOutlineThickness(1.5f);
        controls[i].setOutlineColor(sf::Color(10, 10, 30));
        sf::FloatRect cb = controls[i].getLocalBounds();
        controls[i].setOrigin({cb.position.x + cb.size.x / 2.f, cb.position.y + cb.size.y / 2.f});
        controls[i].setPosition({400.f, cYPos[i]});
    }

    sf::Clock blink;
    bool showInstruction = true;

    while (window.isOpen())
    {
        while (const std::optional<sf::Event> event = window.pollEvent())
        {
            if (event->is<sf::Event::Closed>()) { window.close(); return false; }
            if (auto* key = event->getIf<sf::Event::KeyPressed>())
            {
                if (key->code == sf::Keyboard::Key::Enter) return true;
                if (key->code == sf::Keyboard::Key::Escape) { window.close(); return false; }
            }
        }
        if (blink.getElapsedTime().asSeconds() > 0.5f) { showInstruction = !showInstruction; blink.restart(); }
        window.clear(sf::Color(10, 15, 35));
        window.draw(title);
        window.draw(levelInfo);
        for (int i = 0; i < 3; i++) window.draw(controls[i]);
        if (currentLevel == GameLevel::Level3) window.draw(controls[3]);
        if (showInstruction) window.draw(instruction);
        window.display();
    }
    return false;
}

bool Game::gameOverScreen()
{
    sf::Text title(font, "Game Over!");
    title.setCharacterSize(72);
    title.setFillColor(sf::Color(255, 100, 100));
    title.setOutlineThickness(4.f);
    title.setOutlineColor(sf::Color(10, 10, 30));
    sf::FloatRect tb = title.getLocalBounds();
    title.setOrigin({tb.position.x + tb.size.x / 2.f, tb.position.y + tb.size.y / 2.f});
    title.setPosition({400.f, 150.f});

    sf::Text scoreText(font, "Score: " + std::to_string(score));
    scoreText.setCharacterSize(32);
    scoreText.setFillColor(sf::Color(255, 200, 100));
    scoreText.setOutlineThickness(2.f);
    scoreText.setOutlineColor(sf::Color(10, 10, 30));
    sf::FloatRect sb = scoreText.getLocalBounds();
    scoreText.setOrigin({sb.position.x + sb.size.x / 2.f, sb.position.y + sb.size.y / 2.f});
    scoreText.setPosition({400.f, 280.f});

    sf::Text instruction(font, "Press Enter to restart or ESC to quit");
    instruction.setCharacterSize(22);
    instruction.setFillColor(sf::Color(100, 255, 200));
    instruction.setOutlineThickness(2.f);
    instruction.setOutlineColor(sf::Color(10, 10, 30));
    sf::FloatRect ib = instruction.getLocalBounds();
    instruction.setOrigin({ib.position.x + ib.size.x / 2.f, ib.position.y + ib.size.y / 2.f});
    instruction.setPosition({400.f, 400.f});

    while (window.isOpen())
    {
        while (const std::optional<sf::Event> event = window.pollEvent())
        {
            if (event->is<sf::Event::Closed>()) { window.close(); return false; }
            if (auto* key = event->getIf<sf::Event::KeyPressed>())
            {
                if (key->code == sf::Keyboard::Key::Enter) return true;
                if (key->code == sf::Keyboard::Key::Escape) { window.close(); return false; }
            }
        }
        window.clear(sf::Color(10, 15, 35));
        window.draw(title);
        window.draw(scoreText);
        window.draw(instruction);
        window.display();
    }
    return false;
}

bool Game::checkCollision(const Wall& wall)
{
    sf::FloatRect playerBounds = player.getBounds();
    sf::FloatRect wallBounds = wall.getWallBounds();
    sf::FloatRect holeBounds = wall.getHoleBounds();
    Player::ShapeType playerShape = player.getCurrentShapeType();
    Hole::HoleType holeShape = wall.getHoleType();
    bool shapeMatches = (playerShape == Player::ShapeType::Circle && holeShape == Hole::HoleType::Circle) ||
        (playerShape == Player::ShapeType::Rectangle && holeShape == Hole::HoleType::Rectangle) ||
        (playerShape == Player::ShapeType::Triangle && holeShape == Hole::HoleType::Triangle);
    if (!shapeMatches) return true;
    auto rectanglesIntersect = [](const sf::FloatRect& a, const sf::FloatRect& b) {
        return a.position.x < b.position.x + b.size.x && a.position.x + a.size.x > b.position.x &&
               a.position.y < b.position.y + b.size.y && a.position.y + a.size.y > b.position.y;
    };
    if (!rectanglesIntersect(playerBounds, wallBounds)) return false;
    float overlapLeft = std::max(playerBounds.position.x, holeBounds.position.x);
    float overlapRight = std::min(playerBounds.position.x + playerBounds.size.x, holeBounds.position.x + holeBounds.size.x);
    float overlapTop = std::max(playerBounds.position.y, holeBounds.position.y);
    float overlapBottom = std::min(playerBounds.position.y + playerBounds.size.y, holeBounds.position.y + holeBounds.size.y);
    if (overlapRight <= overlapLeft || overlapBottom <= overlapTop) return true;
    float overlapArea = (overlapRight - overlapLeft) * (overlapBottom - overlapTop);
    float playerArea = playerBounds.size.x * playerBounds.size.y;
    constexpr float REQUIRED_COVERAGE = 0.01f;
    return (overlapArea / playerArea) < REQUIRED_COVERAGE;
}

bool Game::checkObstacleCollision()
{
    sf::FloatRect playerBounds = player.getBounds();
    bool hit = false;
    for (auto it = obstacles.begin(); it != obstacles.end();)
    {
        sf::FloatRect obstacleBounds = (*it)->getBounds();
        bool intersects =
            playerBounds.position.x < obstacleBounds.position.x + obstacleBounds.size.x &&
            playerBounds.position.x + playerBounds.size.x > obstacleBounds.position.x &&
            playerBounds.position.y < obstacleBounds.position.y + obstacleBounds.size.y &&
            playerBounds.position.y + playerBounds.size.y > obstacleBounds.position.y;

        if (intersects)
        {
            hit = true;
            it = obstacles.erase(it);
        }
        else
        {
            ++it;
        }
    }
    return hit;
}

void Game::updateGame(float dt)
{
    player.handleInput();
    player.update(dt);

    if (wallSpawnClock.getElapsedTime().asSeconds() >= getWallSpawnInterval())
    {
        int randHole = rand() % 3;
        walls.push_back(std::make_unique<Wall>(static_cast<Hole::HoleType>(randHole), getWallSpeed()));
        wallSpawnClock.restart();
    }

    if (currentLevel == GameLevel::Level3 && obstacleSpawnClock.getElapsedTime().asSeconds() >= 3.0f)
    {
        const float minX = 140.f;
        const float maxX = 660.f;
        const float safeMargin = 90.f;

        bool spawned = false;
        for (int attempt = 0; attempt < 20 && !spawned; ++attempt)
        {
            float xPos = minX + static_cast<float>(rand()) / RAND_MAX * (maxX - minX);
            bool blocksHole = false;

            for (const auto& w : walls)
            {
                sf::FloatRect wallRect = w->getWallBounds();
                if (wallRect.position.y < -150.f || wallRect.position.y > 600.f)
                    continue;
                    

                float wallLeft = wallRect.position.x;
                float wallRight = wallRect.position.x + wallRect.size.x;
                float safeLeft = wallLeft - safeMargin;
                float safeRight = wallRight + safeMargin;

                if (xPos > safeLeft && xPos < safeRight)
                {
                    blocksHole = true;
                    break;
                }
            }

            if (!blocksHole)
            {
                obstacles.push_back(std::make_unique<Obstacle>(-50.f, getWallSpeed(), xPos));
                spawned = true;
            }
        }

        obstacleSpawnClock.restart();
    }

    for (auto& wall : walls) wall->update(dt);
    for (auto& obstacle : obstacles) obstacle->update(dt);

    walls.erase(std::remove_if(walls.begin(), walls.end(), 
        [](const std::unique_ptr<Wall>& w) { return w->isOffScreen(); }), walls.end());
    obstacles.erase(std::remove_if(obstacles.begin(), obstacles.end(), 
        [](const std::unique_ptr<Obstacle>& o) { return o->isOffScreen(); }), obstacles.end());

    for (auto& heart : heartPickups) heart.update(dt);
    heartPickups.erase(std::remove_if(heartPickups.begin(), heartPickups.end(),
        [](const HeartPickup& heart) { return heart.isOffScreen(); }), heartPickups.end());

    sf::FloatRect playerBounds = player.getBounds();
    heartPickups.erase(std::remove_if(heartPickups.begin(), heartPickups.end(),
        [this, &playerBounds](const HeartPickup& heart)
        {
            sf::FloatRect heartBounds = heart.getBounds();
            bool intersects =
                playerBounds.position.x < heartBounds.position.x + heartBounds.size.x &&
                playerBounds.position.x + playerBounds.size.x > heartBounds.position.x &&
                playerBounds.position.y < heartBounds.position.y + heartBounds.size.y &&
                playerBounds.position.y + playerBounds.size.y > heartBounds.position.y;
            if (intersects && lives < maxLives)
            {
                ++lives;
                return true;
            }
            return false;
        }), heartPickups.end());

    for (auto& fh : fallingHearts) fh.update(dt);
    fallingHearts.erase(std::remove_if(fallingHearts.begin(), fallingHearts.end(),
        [](const FallingHeart& fh) { return fh.isFinished(); }),
        fallingHearts.end());

    for (auto& wall : walls)
    {
        if (!wall->hasBeenChecked() && wall->getWallY() + 50.f >= 525.f)
        {
            wall->markChecked();
            if (checkCollision(*wall))
            {
                if (lives > 0)
                {
                    int oldLives = lives;
                    --lives;

                    float startX = 800.f - 30.f;
                    float yHud = 25.f;
                    float spacing = 25.f;
                    int lostIndex = oldLives - 1;
                    float x = startX - lostIndex * spacing;
                    fallingHearts.emplace_back(sf::Vector2f{x, yHud});
                }

                if (lives <= 0)
                {
                    if (gameOverScreen())
                    {
                        walls.clear();
                        obstacles.clear();
                        heartPickups.clear();
                        wallSpawnClock.restart();
                        obstacleSpawnClock.restart();
                        gameTimeClock.restart();
                        player = Player();
                        score = 0;
                        lives = maxLives;
                        wallsSinceLastHeart = 0;
                        nextHeartSpawnWalls = 6;
                    }
                    else { window.close(); return; }
                }
                break;
            }
            else
            {
                score++;
                wallsSinceLastHeart++;
                if (wallsSinceLastHeart >= nextHeartSpawnWalls)
                {
                    float xPos = static_cast<float>((rand() % 560) + 120);
                    heartPickups.emplace_back(sf::Vector2f{xPos, -30.f});
                    wallsSinceLastHeart = 0;
                    nextHeartSpawnWalls = 6 + (rand() % 2);
                }
            }
        }
    }

    if (currentLevel == GameLevel::Level3 && checkObstacleCollision())
    {
        if (lives > 0)
        {
            int oldLives = lives;
            --lives;

            float startX = 800.f - 30.f;
            float yHud = 25.f;
            float spacing = 25.f;
            int lostIndex = oldLives - 1;
            float x = startX - lostIndex * spacing;
            fallingHearts.emplace_back(sf::Vector2f{x, yHud});
        }

        if (lives <= 0)
        {
            if (gameOverScreen())
            {
                walls.clear();
                obstacles.clear();
                heartPickups.clear();
                wallSpawnClock.restart();
                obstacleSpawnClock.restart();
                gameTimeClock.restart();
                player = Player();
                score = 0;
                lives = maxLives;
                wallsSinceLastHeart = 0;
                nextHeartSpawnWalls = 6;
            }
            else { window.close(); return; }
        }
    }
}

void Game::drawGame()
{
    struct GameStar
    {
        sf::Vector2f pos;
        float radius;
        float phase;
        std::uint8_t baseAlpha;
    };

    static std::vector<GameStar> stars;
    static bool starsInitialized = false;
    static sf::Clock starClock;

    if (!starsInitialized)
    {
        stars.reserve(200);
        for (int i = 0; i < 200; ++i)
        {
            GameStar s;
            s.pos = { static_cast<float>(rand() % 800), static_cast<float>(rand() % 600) };
            s.radius = 0.7f + static_cast<float>(rand() % 9) / 10.f;
            s.phase = static_cast<float>(rand() % 628) / 100.f;
            s.baseAlpha = static_cast<std::uint8_t>(160 + rand() % 80);
            stars.push_back(s);
        }
        starsInitialized = true;
        starClock.restart();
    }

    float t = starClock.getElapsedTime().asSeconds();

    window.clear(sf::Color(2, 4, 10));
    sf::RectangleShape topGrad({800.f, 320.f});
    topGrad.setPosition({0.f, 0.f});
    topGrad.setFillColor(sf::Color(12, 20, 60));
    window.draw(topGrad);
    sf::RectangleShape midGrad({800.f, 180.f});
    midGrad.setPosition({0.f, 220.f});
    midGrad.setFillColor(sf::Color(6, 10, 30));
    window.draw(midGrad);
    sf::RectangleShape bottomGrad({800.f, 200.f});
    bottomGrad.setPosition({0.f, 400.f});
    bottomGrad.setFillColor(sf::Color(3, 3, 14));
    window.draw(bottomGrad);

    sf::CircleShape nebula(260.f);
    nebula.setOrigin({260.f, 260.f});
    nebula.setPosition({190.f, 120.f});
    nebula.setFillColor(sf::Color(90, 40, 140, 90));
    window.draw(nebula);
    nebula.setRadius(220.f);
    nebula.setOrigin({220.f, 220.f});
    nebula.setPosition({620.f, 200.f});
    nebula.setFillColor(sf::Color(40, 150, 180, 75));
    window.draw(nebula);

    for (const auto& s : stars)
    {
        float twinkle = 0.5f + 0.5f * std::sin(t * 1.6f + s.phase);
        std::uint8_t alpha = static_cast<std::uint8_t>(twinkle * s.baseAlpha);
        sf::CircleShape starShape(s.radius);
        starShape.setOrigin({s.radius, s.radius});
        starShape.setPosition(s.pos);
        starShape.setFillColor(sf::Color(235, 240, 255, alpha));
        window.draw(starShape);
    }

    sf::RectangleShape corridorCore({680.f, 130.f});
    corridorCore.setPosition({60.f, 460.f});
    corridorCore.setFillColor(sf::Color(6, 10, 25, 245));
    window.draw(corridorCore);

    sf::RectangleShape corridorGlow({720.f, 160.f});
    corridorGlow.setPosition({40.f, 445.f});
    corridorGlow.setFillColor(sf::Color(40, 120, 190, 40));
    corridorGlow.setOutlineThickness(3.f);
    corridorGlow.setOutlineColor(sf::Color(90, 200, 255, 90));
    window.draw(corridorGlow);

    float scanY = 465.f + std::fmod(t * 40.f, 120.f);
    sf::RectangleShape scan({680.f, 10.f});
    scan.setPosition({60.f, scanY});
    scan.setFillColor(sf::Color(120, 220, 255, 35));
    window.draw(scan);

    sf::RectangleShape hudBar({800.f, 70.f});
    hudBar.setPosition({0.f, 0.f});
    hudBar.setFillColor(sf::Color(3, 3, 18, 235));
    hudBar.setOutlineThickness(0.f);
    window.draw(hudBar);

    window.draw(platform);
    for (auto& wall : walls) wall->draw(window);
    for (auto& obstacle : obstacles) obstacle->draw(window);
    for (auto& heart : heartPickups) heart.draw(window);
    player.draw(window);

    sf::Text scoreText(font, "Score: " + std::to_string(score));
    scoreText.setCharacterSize(24);
    scoreText.setFillColor(sf::Color(255, 220, 140));
    scoreText.setOutlineThickness(2.f);
    scoreText.setOutlineColor(sf::Color(0, 0, 0, 200));
    scoreText.setPosition({20.f, 10.f});
    window.draw(scoreText);

    std::string levelName = currentLevel == GameLevel::Level1 ? "Easy" : 
        currentLevel == GameLevel::Level2 ? "Medium" : "Hard";
    sf::Text levelText(font, "Level: " + levelName);
    levelText.setCharacterSize(20);
    levelText.setFillColor(sf::Color(180, 255, 180));
    levelText.setOutlineThickness(1.5f);
    levelText.setOutlineColor(sf::Color(0, 0, 0, 200));
    levelText.setPosition({20.f, 40.f});
    window.draw(levelText);

    float startX = 800.f - 30.f;
    float y = 25.f;
    float spacing = 25.f;
    for (int i = 0; i < maxLives; ++i)
    {
        sf::CircleShape heartIcon(8.f);
        heartIcon.setOrigin({8.f, 8.f});
        heartIcon.setPosition({startX - i * spacing, y});
        if (i < lives)
            heartIcon.setFillColor(sf::Color(255, 100, 150));
        else
            heartIcon.setFillColor(sf::Color(80, 80, 80));
        window.draw(heartIcon);
    }

    for (const auto& fh : fallingHearts) fh.draw(window);
    window.display();
}

void Game::gameLoop()
{
    sf::Clock deltaClock;
    gameTimeClock.restart();

    while (window.isOpen())
    {
        while (const std::optional<sf::Event> event = window.pollEvent())
        {
            if (event->is<sf::Event::Closed>()) window.close();
        }
        float dt = deltaClock.restart().asSeconds();
        updateGame(dt);
        drawGame();
    }
}