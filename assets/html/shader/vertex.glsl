varying vec2 Point;
    void main()
    {
    vec3 vNormal = ( mat3( modelViewMatrix ) * normal );
    vNormal = normalize(vNormal);
    Point.x = vNormal.x * 0.5 + 0.5;
    Point.y = vNormal.y * 0.5 + 0.5;
    gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );
    }