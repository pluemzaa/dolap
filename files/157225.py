<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test2"/>
        <attribute name="authors" value="ZXN"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 08:21:52 PM"/>
        <attribute name="created" value="WlhOO0xBUFRPUC0yOVVSOFUyVTsyNTY4LTA3LTE2OzA3OjQyOjUyIFBNOzI2MTQ="/>
        <attribute name="edited" value="WlhOO0xBUFRPUC0yOVVSOFUyVTsyNTY4LTA3LTE2OzA4OjIxOjUyIFBNOzc7MjcyNg=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, inte, years, i, total" type="Real" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="inte"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="i" expression="0"/>
            <while expression="i&lt;years">
                <assign variable="total" expression="money*(1+(inte/100))"/>
                <assign variable="money" expression="total"/>
                <output expression="&quot;Year&quot;&amp;(i+1)&amp;&quot;:&quot;&amp; total" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>