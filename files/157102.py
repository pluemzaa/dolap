<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="FlowLab4"/>
        <attribute name="authors" value="Ninen"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:54:47 PM"/>
        <attribute name="created" value="TmluZW47U0FCVFVERTsyMDI1LTA3LTE2OzA0OjQyOjM1IFBNOzIzMDk="/>
        <attribute name="edited" value="TmluZW47U0FCVFVERTsyMDI1LTA3LTE2OzA0OjU0OjQ3IFBNOzE7MjQyMw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, calinterest" type="Real" array="False" size=""/>
            <declare name="interest, year, i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="calinterest" expression="interest/100"/>
            <while expression="i &lt; year">
                <assign variable="i" expression="i+1"/>
                <assign variable="money" expression="money *(1 + calinterest)"/>
                <output expression="&quot;Year &quot; &amp;i&amp; &quot; : &quot; &amp;money" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>