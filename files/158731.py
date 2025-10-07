<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lap4"/>
        <attribute name="authors" value="HP"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 10:58:31 PM"/>
        <attribute name="created" value="SFA7TEFQVE9QLUhROTVETlROOzI1NjgtMDctMjI7MTA6MzM6MTcgUE07MjUyMw=="/>
        <attribute name="edited" value="SFA7TEFQVE9QLUhROTVETlROOzI1NjgtMDctMjI7MTA6NTg6MzEgUE07NTsyNjM4"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest" type="Real" array="False" size=""/>
            <declare name="years, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest(%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input yenrs: &quot;" newline="True"/>
            <input variable="years"/>
            <for variable="i" start="1" end="years" direction="inc" step="1">
                <assign variable="money" expression="money*(1+interest /100)"/>
                <output expression="&quot;years &quot; &amp; i &amp;&quot; &quot;&amp;money" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>