#type
#isinstance
#issubclass
#callable
#getattr
#setattr
#hasattr


from GeoClasses import Place, Geolocation



if __name__ == '__main__':
    p1 = Place(lat=19.4326, lon=-99.1332, description="CDMX")
    p2 = Place(lat=25.7617, lon=-80.1918, description="Miami")
    g1 = Geolocation(lat=19.4326, lon=-99.1332)
    print(p1)
    print(p2)

    if not isinstance(g1, Place):
        print("g1 no es instancia de Place") 

    if type(p1) is Place:
        print("p1 es exactamente una instancia de Place")
    else:
        print("p1 no es exactamente una instancia de Place")


    if isinstance(p1, Geolocation):
        print("Es una instancia de Geolocation") 
    
    if issubclass(Place, Geolocation):
        print("Place es subclase de Geolocation")

    if(hasattr(p1, "lat")):
        print("si lo tiene: ", getattr(p1, "lat"))
    
    if(hasattr(p1, "distance")):
        print("si tiene algo llamado distance")
        method = getattr(p1, "distance")
        if callable(method):
            result = method(p2)  
            print("Distance: ", result)
    
    """
    print(p1.__class__)
    print(p2.__class__)
    """