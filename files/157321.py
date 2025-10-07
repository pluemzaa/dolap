<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="222"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-19 01:53:39 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzozNDoxMCBQTTsyNTQw"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xOTswMTo1MzozOSBQTTsyMDsyNzA5"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="x, y, c, t, koi, lop, kop" type="Integer" array="False" size=""/>
            <assign variable="c" expression="25"/>
            <assign variable="t" expression="20"/>
            <assign variable="lop" expression="0"/>
            <assign variable="kop" expression="10"/>
            <output expression="&quot;Beverage List: &quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: &quot;&amp;kop" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: &quot;&amp;lop" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="x"/>
            <if expression="x==1">
                <then>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="y"/>
                    <if expression="y&lt;=kop">
                        <then>
                            <output expression="&quot;You purchased Coffee &quot;" newline="True"/>
                            <assign variable="koi" expression="y*c"/>
                            <output expression="&quot;Total Price: &quot;&amp;koi&amp;&quot; Baht &quot;" newline="True"/>
                            <output expression="&quot;Enjoy! &quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="x==2">
                        <then>
                            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                            <input variable="y"/>
                            <if expression="y&lt;=lop">
                                <then>
                                    <output expression="&quot;You purchased Coffee &quot;" newline="True"/>
                                    <assign variable="koi" expression="y*t"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else/>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>