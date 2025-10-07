<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="AAAA2"/>
        <attribute name="authors" value="Sumat"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 05:10:11 PM"/>
        <attribute name="created" value="U3VtYXQ7VE9OR19UT05HX1NIVVI7MjU2OC0wNy0xNjswNDo0NDo1NyBQTTsyOTYx"/>
        <attribute name="edited" value="U3VtYXQ7VE9OR19UT05HX1NIVVI7MjU2OC0wNy0xNjswNToxMDoxMSBQTTsxOzMwNTM="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="teaStock, coffeeStock, oder, qua" type="Integer" array="False" size=""/>
            <assign variable="coffeeStock" expression="10"/>
            <assign variable="teaStock" expression="0"/>
            <output expression="&quot;Beverage List:&quot; &amp; toChar(13)&amp;&#13;&#10;&quot;1. Coffee - 25 Baht - Qty: 10&quot;&amp; toChar(13)&amp;&#13;&#10;&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="oder"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="qua"/>
            <if expression="oder == 1">
                <then>
                    <if expression="!(qua &gt; coffeeStock)">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot;&amp; qua*25 &amp;&quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="!(qua&gt;teaStock)">
                        <then>
                            <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot;&amp; qua*20 &amp;&quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>