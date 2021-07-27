using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Flock : MonoBehaviour
{
    public FlockAgent agentPrefab;
    public float slope;
    public float threshold;
    public float MaxValue;
    public float X;
    public float Z;
    public float c1;
    public float c2;
    public float c3;
    public float c4;
    public Vector3 Team_vector;
    List<FlockAgent> agents = new List<FlockAgent>();
    public float team_best = -999999;
    public FlockBehaviour behaviour;
    [Range(0, 30)]
    public int StartingCount = 20;
   
    
    public float Attribute(float slope, float threshold, float X, float Z, float x, float z, float MaxValue)
    {

        float distance = (x - X) * (x - X) + (z - Z) * (z - Z);
        float Multiplier;
        if (distance < threshold * threshold)
        {
            Multiplier = MaxValue - (slope) * (Mathf.Sqrt(distance));
        }
        else
        {
             Multiplier = (MaxValue - (slope) * (threshold)) / (distance);
            
        }
        return Multiplier;
    }
    public Vector3 ObstacleMove(List<FlockAgent> agents)
    {return Vector3.zero;}
    // Start is called before the first frame update
    void Start()
    {
        
        for(int i = 0; i < StartingCount; i++) 
        {
            float x,z;
            x = Random.Range(-45f, 45f);
            z = Random.Range(-45f, 45f);
            FlockAgent newAgent = Instantiate(
                agentPrefab,
                new Vector3(x, 0, z),
                Quaternion.Euler(Vector3.forward),
                transform
                ) ;
            newAgent.name = "Agent" + i;
            newAgent.Current = new Vector3(Random.Range(-1f, 1f), 0, Random.Range(-1f, 1f)).normalized;
            agents.Add(newAgent);

            
        }
        foreach (FlockAgent agent in agents)
        {
            float f= Attribute(slope, threshold, X, Z, agent.transform.position.x, agent.transform.position.z, MaxValue);
            if (f > team_best) { team_best = f; Team_vector = agent.transform.position; }
            agent.Personal = f;




        }


    }

    // Update is called once per frame
    void Update()
    {
        foreach (FlockAgent agent in agents) 
        {
            
            float f = Attribute(slope,threshold,X,Z,agent.transform.position.x,agent.transform.position.z,MaxValue);
            if(f > team_best) { team_best=f; Team_vector = agent.transform.position; }
            if (f > agent.Personal) { agent.Personal = f; agent.Personal_vector = agent.transform.position; }
            agent.Current = c1 * ((Team_vector - agent.transform.position).normalized) + c2 * (agent.Current.normalized) + c3 * ((agent.Personal_vector - agent.transform.position).normalized)+c4*(new Vector3(Random.Range(-1f,1f),0,Random.Range(-1f,1f)).normalized);
            agent.Move(agent.Current.normalized * 5);
        }
        


        
    }
}
