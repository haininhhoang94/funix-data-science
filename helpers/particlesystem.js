class Particle {
  constructor(x, y) {
    //HaiNH: based on your lecture, the vector (particle) should have
    // the following feature
    this.position = createVector(x, y);
    this.velocity = createVector(0, 0);
    this.acceleration = createVector(0, 0);
    // HaiNH: 0 because we would calculate this later
    // this.mass = 1;
    // Assume mass = 1
  }
  applyForce(force) {
    // HaiNH: hint: p below have both run and applyForce
    // function, thus our Particle need to have both 
    // run and applyForce to represent a particle feature
    this.acceleration.add(force);
  }

  update_feature() {
    this.velocity.add(this.acceleration);
    this.position.add(this.velocity);
    this.acceleration.mult(0);
  }
  // HaiNH: for visualization
  run() {
    fill(255);
    ellipse(this.position.x, this.position.y, 10, 10);
  }
}

class ParticleSystem {

  constructor() {
    this.particles = [];
    this.G = 0.5;
  }

  addParticle(x, y) {
    this.particles.push(new Particle(x, y));
  }

  applyForce() {
    // HaiNH: temporary merge applyForce and calculateForce, think about this later....
    // YOUR CODE HERE
    // that calculates gravitational forces and applies them to particles.
    // Gravitational forces are pair-wise. Each unique pairing of two particles.
    // They are equal but opposite: particle A exerts a force on particle B 
    // while particle B exerts that same amount of force on A (but in the opposite direction!).
    for (let i = 0; i < this.particles.length; i++) {
      for (let j = i + 1; j < this.particles.length; j++) {
        // Pair A-B each possible pair
        const particleA = this.particles[i];
        const particleB = this.particles[j];
        // Calculate distance btw particle
        const force = p5.Vector.sub(particleB.position, particleA.position); // force is a vector cause mass to accelerate - hence distance
        const strg = (this.G * particleA.mass * particleB.mass) / (force.magSq());
        // Review Gravity Equation in lecture
        force.setMag(strg);
        particleA.applyForce(force);
        particleB.applyForce(force.mult(-1));
      }
    }
  }

  run() {
    for (const p of this.particles) {
      p.update_feature();
      p.run();
    }
  }
}

let particleSystem;
function setup() {
  createCanvas(1000, 1000);
  particleSystem = new ParticleSystem();
  // Add particles to the system
  particleSystem.addParticle(150, 100);
  particleSystem.addParticle(200, 200);
  particleSystem.addParticle(350, 300);
  particleSystem.addParticle(430, 400);
  particleSystem.addParticle(580, 500);
  particleSystem.addParticle(670, 600);
  particleSystem.addParticle(790, 700);
  particleSystem.addParticle(800, 880);
  particleSystem.addParticle(910, 900);
}
function draw() {
  background(0);

  // Apply forces to the particles
  // particleSystem.applyForce(particleSystem.calculateForce());
  particleSystem.applyForce();
  // Run the particle system
  particleSystem.run();
}
