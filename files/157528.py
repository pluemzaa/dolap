<?xml version="1.0"?>
<flowgorithm fileversion="4.0">
    <attributes>
        <attribute name="name" value="683380471-6"/>
        <attribute name="authors" value="HP"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 08:24:30 PM"/>
        <attribute name="created" value="SFA7V0lOMTE7MjU2OC0wNy0yMDswNzoyMzoyMiBQTTsxNzc4"/>
        <attribute name="edited" value="SFA7V0lOMTE7MjU2OC0wNy0yMDswODoyNDozMCBQTTsxOzE4ODc="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, qty, totalprice, coffeeprice, teaprice, coffeeqty, teaqty" type="Integer" array="False" size=""/>
            <assign variable="coffeeprice" expression="25"/>
            <assign variable="teaprice" expression="20"/>
            <assign variable="coffeeqty" expression="10"/>
            <assign variable="teaqty" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="qty"/>
            <if expression="menu==1">
                <then>
                    <if expression="qty&gt;coffeeqty">
                        <then>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <assign variable="totalprice" expression="qty * coffeeprice"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot; Total Price: &quot;&amp;totalprice&amp;&quot; Baht &quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="qty&gt;teaqty">
                        <then>
                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <assign variable="totalprice" expression="qty * coffeeprice"/>
                            <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                            <output expression="&quot; Total Price: &quot;&amp;totalprice&amp;&quot; Baht &quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>