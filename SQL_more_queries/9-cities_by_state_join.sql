-- Lists all cities contained in the database hbtn_0d_usa
SELECT states.id, states.name, states.state_id FROM cities
LEFT JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;