<?xml version="1.0"?>
<flowgorithm fileversion="3.0">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="bamboo"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 12:49:13 "/>
        <attribute name="created" value="YmFtYm9vO01BQ0JPT0tBSVJCQU07MjU2OC0wNy0yMjsiMTI6MTM6MjYgIjsyNzYy"/>
        <attribute name="edited" value="YmFtYm9vO01BQ0JPT0tBSVJCQU07MjU2OC0wNy0yMjsiMTI6NDk6MTMgIjsyOzI4NzY="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, quantity, totalPriceCoffee, totallPriceTea" type="Integer" array="False" size=""/>
            <output expression="&quot; Beverage List: &quot;" newline="True"/>
            <output expression="&quot; 1. Coffee - 25 Baht - Qty: 10 &quot;" newline="True"/>
            <output expression="&quot; 2. Tea - 20 Baht - Qty: 0 &quot;" newline="True"/>
            <output expression="&quot; Select menu (1 = coffee,  2  = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot; Enter quantity: &quot;" newline="True"/>
            <input variable="quantity"/>
            <if expression="menu == 1">
                <then>
                    <if expression="Quantity &lt;= 10">
                        <then>
                            <assign variable="totalPriceCoffee" expression="Quantity * 25"/>
                            <output expression="&quot; You purchased Coffee &quot;" newline="True"/>
                            <output expression="&quot; Total Price : &quot;&amp; totalPriceCoffee &amp; &quot; Baht&quot;" newline="True"/>
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
                            <if expression="Quantity &gt; 0">
                                <then>
                                    <output expression="&quot; sorry, Tea out of stock, &quot;" newline="True"/>
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