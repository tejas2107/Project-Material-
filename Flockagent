using System.Collections;
using System.Collections.Generic;
using UnityEngine;
[RequireComponent(typeof(Collider))]
public class FlockAgent : MonoBehaviour
{
    Collider agentCollider;
    public int NumberOfRays = 20;
    public int TargetVelocity = 4;
    float angle = 180;
    public float ray_range = 2f;
    public float personal;
    public Vector3 Current;
    public Vector3 Personal_vector;
    

    public Collider AgentCollider{ get { return AgentCollider; } }
    public float Personal { get { return personal; } set { personal = value; } }

    // Start is called before the first frame update
    void Start()
    {
        agentCollider = GetComponent<Collider>();

    }

    // Update is called once per frame
    public void Move(Vector3 velocity)
    {
        var ray1 = new Ray(this.transform.position,Current);
        if (Physics.Raycast(ray1, 2))
        {
            var deltaPosition = Vector3.zero;
            for (int i = 0; i < NumberOfRays; i++)
            {
                var rotation = this.transform.rotation;
                var RotationMod = Quaternion.AngleAxis((i / ((float)NumberOfRays - 1)) * angle * 2 - angle, this.transform.up);
                var direction = rotation * RotationMod *Current;
                RaycastHit hitInfo;


                var ray = new Ray(this.transform.position, direction);
                if (Physics.Raycast(ray, out hitInfo, ray_range))
                {
                    deltaPosition -= (1.0f / NumberOfRays) * TargetVelocity * direction;

                }
                else
                {
                    deltaPosition += (1.0f / NumberOfRays) * TargetVelocity * direction;
                }
                this.transform.position += deltaPosition * Time.deltaTime;

            }
        }
        else
        { this.transform.position += velocity * Time.deltaTime;}


    }

}
