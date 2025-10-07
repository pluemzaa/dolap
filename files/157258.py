<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="awwet"/>
        <attribute name="authors" value="Anurak"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-21 08:04:04 PM"/>
        <attribute name="created" value="QW51cmFrO05BWTsyNTY4LTA3LTIxOzA3OjUwOjI5IFBNOzIxNDA="/>
        <attribute name="edited" value="QW51cmFrO05BWTsyNTY4LTA3LTIxOzA4OjA0OjA0IFBNOzI7MjI0Mg=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest" type="Real" array="False" size=""/>
            <declare name="years, i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <assign variable="years" expression="3"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <while expression="i&lt;years">
                <assign variable="money" expression="money*(1 + interest/100)"/>
                <output expression="&quot;Year &quot; &amp; (i+1) &amp; &quot;: &quot; &amp; money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>