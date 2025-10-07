<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="flowLab2"/>
        <attribute name="authors" value="Ninen"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:32:01 PM"/>
        <attribute name="created" value="TmluZW47U0FCVFVERTsyMDI1LTA3LTE2OzA0OjEwOjM5IFBNOzIzMDg="/>
        <attribute name="edited" value="TmluZW47U0FCVFVERTsyMDI1LTA3LTE2OzA0OjMyOjAxIFBNOzE7MjQwOQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="coffee, tea, menu, quan, total" type="Integer" array="False" size=""/>
            <assign variable="coffee" expression="10"/>
            <assign variable="tea" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: &quot; &amp;coffee" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: &quot; &amp;tea" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu == 1">
                <then>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="quan"/>
                    <if expression="quan &lt;= coffee">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="total" expression="quan*25"/>
                            <output expression="&quot;Total Price : &quot; &amp;total&amp; &quot; Baht&quot;" newline="True"/>
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
                            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                            <input variable="quan"/>
                            <if expression="quan &lt;= tea">
                                <then>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <assign variable="total" expression="quan*20"/>
                                    <output expression="&quot;Total Price : &quot; &amp;total&amp; &quot; Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else>
                            <output expression="&quot;Invalid menu&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>