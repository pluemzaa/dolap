<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_2"/>
        <attribute name="authors" value="Staff"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 01:00:28 PM"/>
        <attribute name="created" value="U3RhZmY7REVTS1RPUC1IUEtPSzhSOzI1NjgtMDctMTg7MTA6NDQ6NDggQU07Mjg4OQ=="/>
        <attribute name="edited" value="U3RhZmY7REVTS1RPUC1IUEtPSzhSOzI1NjgtMDctMjA7MDE6MDA6MjggUE07MjsyOTk2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, quantity, totalPriceCoffee, totalPriceTea" type="Integer" array="False" size=""/>
            <output expression="&quot;Beverage List: &quot;" newline="True"/>
            <output expression="&quot; 1. Coffee - 25 Baht - Qty: 10 &quot;" newline="True"/>
            <output expression="&quot; 2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot; Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot; Enter quantity: &quot;" newline="True"/>
            <input variable="quantity"/>
            <if expression="menu == 1">
                <then>
                    <if expression="quantity &lt;= 10">
                        <then>
                            <assign variable="totalPriceCoffee" expression="quantity * 25"/>
                            <output expression="&quot; You purchased Coffee &quot;" newline="True"/>
                            <output expression="&quot; Total Price: &quot; &amp; totalPriceCoffee &amp; &quot; Baht &quot;" newline="True"/>
                            <output expression="&quot; Enjoy! &quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot; Sorry, Coffee out of stock &quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu == 2">
                        <then>
                            <if expression="quantity &gt; 0">
                                <then>
                                    <output expression="&quot; Sorry, Tea out of stock &quot;" newline="True"/>
                                </then>
                                <else/>
                            </if>
                        </then>
                        <else/>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>