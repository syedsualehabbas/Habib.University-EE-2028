#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include <vector>
#include <optional>
#include <cstdlib>
#include <algorithm>
#include <variant>

class Game
{
private:
    sf::RenderWindow window;
    sf::Font font;
    bool isRunning;
    sf::ConvexShape platform;
    enum class PlayerShapeType { Circle, Rect, Triangle };

    std::variant<sf::CircleShape, sf::RectangleShape, sf::ConvexShape> playerShape;
    PlayerShapeType currentShape = PlayerShapeType::Rect;


    // --- Game objects ---
    enum class HoleType { Circle, Rect, Triangle };

    struct Wall {
        sf::RectangleShape wall;
        std::variant<sf::CircleShape, sf::RectangleShape, sf::ConvexShape> hole;
        HoleType holeType;
        float speed;
        bool checked = false;
    };

    std::vector<Wall> walls;
    sf::Clock wallSpawnClock;

public:
    Game() : window(sf::VideoMode({800, 600}), "Shape Shifter Run"), isRunning(true) {
        window.setFramerateLimit(60);

        if (!font.openFromFile("arial.ttf")){
            printf("Failed to load arial.ttf\n");
        }

        // ----- Perspective Platform (Trapezoid) -----
        platform.setPointCount(4);

        // Bottom-left (nearest to camera)
        platform.setPoint(0, {50.f, 600.f});

        // Bottom-right
        platform.setPoint(1, {750.f, 600.f});

        // Top-right (far away, narrow width)
        platform.setPoint(2, {520.f, 300.f});

        // Top-left
        platform.setPoint(3, {280.f, 300.f});

        platform.setFillColor(sf::Color(80, 80, 120));


        // ----- Player entity -----
        playerShape = createPlayerShape(currentShape);

        // place at same position as before
        std::visit([&](auto& s) {
            s.setPosition({400.f, 525.f});
        }, playerShape);

        
    }

    void run()
    {
        if (welcomeScreen())
            gameLoop();
    }

private:
    //-----------------------------------------------------------------------
    //  WELCOME SCREEN (unchanged)
    //-----------------------------------------------------------------------
    bool welcomeScreen()
    {
        sf::Text title(font, "Welcome to Shape Shifter Run");
        title.setCharacterSize(48);
        title.setFillColor(sf::Color::White);

        sf::FloatRect tb = title.getLocalBounds();
        title.setOrigin({tb.position.x + tb.size.x / 2.f,
                         tb.position.y + tb.size.y / 2.f});
        title.setPosition({400.f, 250.f});

        sf::Text instruction(font, "Press Enter to start the game");
        instruction.setCharacterSize(24);
        instruction.setFillColor(sf::Color(200,200,200));

        sf::FloatRect ib = instruction.getLocalBounds();
        instruction.setOrigin({ib.position.x + ib.size.x / 2.f,
                               ib.position.y + ib.size.y / 2.f});
        instruction.setPosition({400.f, 350.f});

        sf::Clock blink;
        bool showInstruction = true;

        while (window.isOpen())
        {
            while (const std::optional<sf::Event> event = window.pollEvent())
            {
                if (event->is<sf::Event::Closed>())
                {
                    window.close();
                    return false;
                }

                if (auto* key = event->getIf<sf::Event::KeyPressed>())
                {
                    if (key->code == sf::Keyboard::Key::Enter)
                        return true;

                    if (key->code == sf::Keyboard::Key::Escape)
                    {
                        window.close();
                        return false;
                    }
                }
            }

            if (blink.getElapsedTime().asSeconds() > 0.5f)
            {
                showInstruction = !showInstruction;
                blink.restart();
            }

            window.clear(sf::Color(20, 20, 40));
            window.draw(title);
            if (showInstruction)
                window.draw(instruction);
            window.display();
        }
        return false;
    }

    //-----------------------------------------------------------------------
    //  CREATE HOLE SHAPE
    //-----------------------------------------------------------------------
    std::variant<sf::CircleShape, sf::RectangleShape, sf::ConvexShape>
    createHole(HoleType type)
    {
        switch (type)
        {
            case HoleType::Circle: {
                sf::CircleShape c(50.f);
                c.setOrigin({50.f, 50.f});
                c.setFillColor(sf::Color::Black);
                return c;
            }

            case HoleType::Rect: {
                sf::RectangleShape r({120.f, 60.f});
                r.setOrigin({60.f, 30.f});
                r.setFillColor(sf::Color::Black);
                return r;
            }

            case HoleType::Triangle: {
                sf::ConvexShape tri;
                tri.setPointCount(3);
                tri.setPoint(0, {0.f, -60.f});
                tri.setPoint(1, {-50.f, 40.f});
                tri.setPoint(2, {50.f, 40.f});
                tri.setFillColor(sf::Color::Black);
                tri.setOrigin({0.f, 0.f});
                return tri;
            }
        }

        // fallback
        return sf::CircleShape(50.f);
    }

    std::variant<sf::CircleShape, sf::RectangleShape, sf::ConvexShape>
    createPlayerShape(PlayerShapeType type)
    {
        switch (type)
        {
            case PlayerShapeType::Circle: {
                sf::CircleShape c(40.f);
                c.setOrigin({40.f, 40.f});
                c.setFillColor(sf::Color(255, 200, 120));
                return c;
            }

            case PlayerShapeType::Rect: {
                sf::RectangleShape r({100.f, 50.f});
                r.setOrigin({50.f, 25.f});
                r.setFillColor(sf::Color(255, 200, 120));
                return r;
            }

            case PlayerShapeType::Triangle: {
                sf::ConvexShape t;
                t.setPointCount(3);
                t.setPoint(0, {0.f, -55.f});
                t.setPoint(1, {-45.f, 35.f});
                t.setPoint(2, {45.f, 35.f});
                t.setFillColor(sf::Color(255, 200, 120));
                t.setOrigin({0.f, 0.f});
                return t;
            }
        }

        return sf::CircleShape(40.f);
    }


    //-----------------------------------------------------------------------
    //  SPAWN WALL + RANDOM HOLE
    //-----------------------------------------------------------------------
    void spawnWall()
    {
        Wall w;

        // Base rectangle wall
        float baseWidth = 500.f;
        float baseHeight = 120.f;

        w.wall.setSize({baseWidth, baseHeight});
        w.wall.setFillColor(sf::Color(180, 180, 255));
        w.wall.setOrigin({baseWidth / 2.f, baseHeight / 2.f});
        w.wall.setPosition({400.f, -100.f});

        float startScale = 0.2f;
        w.wall.setScale({startScale, startScale});

        // Pick random hole type
        int r = rand() % 3;
        w.holeType = static_cast<HoleType>(r);
        w.hole = createHole(w.holeType);

        // Place hole initially inside wall center
        std::visit([&](auto& h){
            h.setPosition(w.wall.getPosition());
            h.setScale({startScale, startScale});
        }, w.hole);

        w.speed = 245.f;

        walls.push_back(w);
    }

    //-----------------------------------------------------------------------
    //  UPDATE GAME (movement + scaling)
    //-----------------------------------------------------------------------
    void updateGame(float dt)
    {
        if (wallSpawnClock.getElapsedTime().asSeconds() >= 1.8f)
        {
            spawnWall();
            wallSpawnClock.restart();
        }

        for (auto& w : walls)
        {
            // Move wall
            w.wall.move({0.f, w.speed * dt});

            float y = w.wall.getPosition().y;
            float scale = std::min(1.8f, 0.0025f * y);
            if (scale < 0.15f) scale = 0.15f;

            // Apply scale to wall
            w.wall.setScale({scale, scale});

            // Apply identical scale + position to hole
            std::visit([&](auto& h){
                h.setScale({scale, scale});
                h.setPosition(w.wall.getPosition());
            }, w.hole);
        }

        // Remove off-screen walls
        walls.erase(
            std::remove_if(walls.begin(), walls.end(),
                [&](const Wall& w){ return w.wall.getPosition().y > 900.f; }),
            walls.end()
        );

        // Player depth Y (center) - matches where your player sits
        const float playerY = 525.f;
        const float checkTolerance = 8.f; // small window to consider "at the player"

        // After moving+scaling, check each wall once when it reaches/passes player's Y
        for (auto &w : walls)
        {
            if (w.checked) continue; // already checked this wall

            float wallY = w.wall.getPosition().y;

            // Check if wall center has reached or passed player's Y (only then check)
            if (wallY >= (playerY - checkTolerance))
            {
                w.checked = true; // mark as processed

                // Decide whether to trigger Game Over
                if (shouldTriggerGameOver(w))
                {
                    bool restart = gameOverScreen();
                    if (restart)
                    {
                        walls.clear();
                        wallSpawnClock.restart();
                        // reset player shape & pos in case user changed during gameover
                        playerShape = createPlayerShape(currentShape);
                        std::visit([&](auto &s){ s.setPosition({400.f, 525.f}); }, playerShape);
                    }
                    else
                    {
                        window.close();
                        return; // early exit from updateGame
                    }
                    break; // only handle one collision per frame
                }
            }
        }
    }
    
    //-----------------------------------------------------------------------
    //  DRAW GAME
    //-----------------------------------------------------------------------
    void drawGame()
    {
        window.clear(sf::Color(10, 10, 20));

        // Draw platform first
        window.draw(platform);

        // Draw player
        std::visit([&](auto& s){ window.draw(s); }, playerShape);


        // Hole-subtract blend mode (alpha erase)
        sf::BlendMode eraseAlpha(
            sf::BlendMode::Factor::Zero, sf::BlendMode::Factor::OneMinusSrcAlpha, sf::BlendMode::Equation::Add,
            sf::BlendMode::Factor::Zero, sf::BlendMode::Factor::OneMinusSrcAlpha, sf::BlendMode::Equation::Add
        );

        // Draw all the walls with cutout
        for (auto& w : walls)
        {
            sf::RenderTexture rt({800, 600});
            rt.clear(sf::Color::Transparent);

            rt.draw(w.wall);

            std::visit([&](auto& h) {
                rt.draw(h, sf::RenderStates(eraseAlpha));
            }, w.hole);

            rt.display();

            sf::Sprite finalSprite(rt.getTexture());
            window.draw(finalSprite);
        }

        window.display();
    }


    //-----------------------------------------------------------------------
    //  COLLISION DETECTION
    //-----------------------------------------------------------------------
    // Returns true if player's global bounds are fully inside the hole's global bounds (conservative)
    bool isPlayerInsideHole(const Wall &w)
    {
        sf::FloatRect holeBounds;
        std::visit([&](auto &h) {
            holeBounds = h.getGlobalBounds();
        }, w.hole);

        // get player bounds
        sf::FloatRect playerBounds;
        std::visit([&](auto &p) {
            playerBounds = p.getGlobalBounds();
        }, playerShape);

        // small margin to avoid strict equality issues
        const float margin = 2.0f;

        // SFML 3 FloatRect uses position/size
        float holeLeft  = holeBounds.position.x + margin;
        float holeRight = holeBounds.position.x + holeBounds.size.x - margin;
        float holeTop   = holeBounds.position.y + margin;
        float holeBottom= holeBounds.position.y + holeBounds.size.y - margin;

        float playerLeft  = playerBounds.position.x;
        float playerRight = playerBounds.position.x + playerBounds.size.x;
        float playerTop   = playerBounds.position.y;
        float playerBottom= playerBounds.position.y + playerBounds.size.y;

        return (playerLeft >= holeLeft) && (playerRight <= holeRight)
            && (playerTop >= holeTop) && (playerBottom <= holeBottom);
    }

    // Check whether this wall should trigger Game Over; only call when wall reaches player's depth
    bool shouldTriggerGameOver(const Wall &w)
    {
        // If hole type and player shape mismatch -> immediate fail
        bool shapeMatches = false;
        switch (w.holeType) {
            case HoleType::Circle:shapeMatches = (currentShape == PlayerShapeType::Circle); break;
            case HoleType::Rect:shapeMatches = (currentShape == PlayerShapeType::Rect);   break;
            case HoleType::Triangle: shapeMatches = (currentShape == PlayerShapeType::Triangle); break;
        }

        if (!shapeMatches) return true; // Game over: wrong shape

        // If shapes match, check that the player fits inside the hole geometry (conservative bounding-box test)
        if (!isPlayerInsideHole(w)) return true; // Game over: doesn't physically fit

        // OK: shape matches and player fits
        return false;
    }




    //-----------------------------------------------------------------------
    //  GAME OVER SCREEN
    //-----------------------------------------------------------------------
    bool gameOverScreen()
    {
        sf::Text title(font, "Game Over");
        title.setCharacterSize(64);
        title.setFillColor(sf::Color::Red);
        sf::FloatRect tb = title.getLocalBounds();
        title.setOrigin({tb.position.x + tb.size.x / 2.f, tb.position.y + tb.size.y / 2.f});
        title.setPosition({400.f, 250.f});

        sf::Text instruction(font, "Press Enter to restart the game");
        instruction.setCharacterSize(24);
        instruction.setFillColor(sf::Color(200,200,200));
        sf::FloatRect ib = instruction.getLocalBounds();
        instruction.setOrigin({ib.position.x + ib.size.x / 2.f, ib.position.y + ib.size.y / 2.f});
        instruction.setPosition({400.f, 350.f});


        while (window.isOpen())
        {
            while (const std::optional<sf::Event> event = window.pollEvent())
            {
                if (event->is<sf::Event::Closed>())
                {
                    window.close();
                    return false;
                }

                if (auto* key = event->getIf<sf::Event::KeyPressed>())
                {
                    if (key->code == sf::Keyboard::Key::Enter)
                        return true; // restart
                }
            }

            window.clear(sf::Color(10,10,20));
            window.draw(title);
            window.draw(instruction);
            window.display();
        }
        return false;
    }



    //-----------------------------------------------------------------------
    //  GAME LOOP
    //-----------------------------------------------------------------------
    void gameLoop()
    {
        sf::Clock deltaClock;

        while (window.isOpen())
        {
            while (const std::optional<sf::Event> event = window.pollEvent())
            {
                if (event->is<sf::Event::Closed>()){
                    window.close();
                }

                if (auto* key = event->getIf<sf::Event::KeyPressed>())
                {
                    if (key->code == sf::Keyboard::Key::Num1)
                        currentShape = PlayerShapeType::Circle;
                    if (key->code == sf::Keyboard::Key::Num2)
                        currentShape = PlayerShapeType::Rect;
                    if (key->code == sf::Keyboard::Key::Num3)
                        currentShape = PlayerShapeType::Triangle;

                    playerShape = createPlayerShape(currentShape);

                    // keep position consistent
                    std::visit([&](auto& s) {
                        s.setPosition({400.f, 525.f});
                    }, playerShape);
                }

                
            }

            float dt = deltaClock.restart().asSeconds();
            updateGame(dt);
            drawGame();
        }
    }
};

int main()
{
    Game g;
    g.run();
    return 0;
}