<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Tea out of stock"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-18 11:33:45 AM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtVUYzQlNVRDM7MjU2OC0wNy0xODsxMToxMToyOCBBTTsyNzYz"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtVUYzQlNVRDM7MjU2OC0wNy0xODsxMTozMzo0NSBBTTsxOzI4NzQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="cofree" type="Integer" array="False" size=""/>
            <declare name="Tea" type="Integer" array="False" size=""/>
            <assign variable="Tea" expression="10"/>
            <declare name="menu" type="Integer" array="False" size=""/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu==1">
                <then>
                    <declare name="Coffeeprice" type="Integer" array="False" size=""/>
                    <declare name="nCoffee" type="Integer" array="False" size=""/>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="nCoffee"/>
                    <if expression="(10 - nCoffee)&gt;=0">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="Coffeeprice" expression="nCoffee*25"/>
                            <output expression="&quot;Total Price: &quot; &amp; Coffeeprice &amp; &quot;Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <declare name="atea" type="Integer" array="False" size=""/>
                    <declare name="ntea" type="Integer" array="False" size=""/>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="ntea"/>
                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>