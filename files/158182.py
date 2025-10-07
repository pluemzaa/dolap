<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="flowchartlab4"/>
        <attribute name="authors" value="WINDOWS"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 12:03:28 AM"/>
        <attribute name="created" value="V0lORE9XUztMQVBUT1AtRjFJVDVWRlY7MjU2OC0wNy0yMTswODozMjo1MiBQTTsyOTMw"/>
        <attribute name="edited" value="V0lORE9XUztMQVBUT1AtRjFJVDVWRlY7MjU2OC0wNy0yMjsxMjowMzoyOCBBTTsxMTszMDY5"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="cf, te, Finc, Fint, menu, Number, c, f" type="Real" array="False" size=""/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <assign variable="cf" expression="10"/>
            <assign variable="te" expression="0"/>
            <assign variable="c" expression="25"/>
            <assign variable="f" expression="20"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="Number"/>
            <if expression="menu == 1">
                <then>
                    <if expression="cf &gt;= Number">
                        <then>
                            <assign variable="Finc" expression="Number * c"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price :&quot;&amp;Finc&amp;&quot;Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu == 2">
                        <then>
                            <if expression="te &gt;= Number">
                                <then>
                                    <assign variable="Fint" expression="Number * f"/>
                                    <output expression="&quot;You purchased tea&quot;" newline="True"/>
                                    <output expression="&quot;Total Price :&quot;&amp;Fint&amp;&quot;Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </else>
                            </if>
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