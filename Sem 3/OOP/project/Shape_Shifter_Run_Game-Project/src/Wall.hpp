#ifndef WALL_HPP
#define WALL_HPP

#include <SFML/Graphics.hpp>
#include <memory>
#include "Hole.hpp"

class Wall
{
public:
    Wall(Hole::HoleType holeType, float wallSpeed);
    void update(float dt);
    void draw(sf::RenderWindow& window);
    bool isOffScreen() const;
    bool hasBeenChecked() const { return checked; }
    void markChecked() { checked = true; }
    sf::FloatRect getWallBounds() const;
    sf::FloatRect getHoleBounds() const;
    Hole::HoleType getHoleType() const;
    float getWallY() const;
private:
    sf::RectangleShape wall;
    std::unique_ptr<Hole> hole;
    float speed;
    bool checked = false;
    sf::Color wallColor;
};

#endif // WALL_HPP