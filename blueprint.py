from constructs.ecs import ECS

class Blueprint():

    def __init__(self) -> None:

        ecsApp = ECS(name='web-app', age='33')
        print(ecsApp.say_hi())

        ecsProxy = ECS()
        print(ecsProxy.say_hi())

        print(ecsApp.get_from_log_group())
        print(ecsProxy.get_from_log_group())